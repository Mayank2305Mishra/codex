import streamlit as st
from google import generativeai as genai
import time
import tempfile
from pathlib import Path
import logging
from prompt import analysis_prompt
from dotenv import load_dotenv
import os

load_dotenv(".env")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")


logging.basicConfig(level=logging.INFO)

try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception:
    st.error("🚨 Google API Key not found. Please set it in your Streamlit secrets (`.streamlit/secrets.toml`).")
    st.stop()

# Constants
NUMBER_OF_MESSAGES_TO_DISPLAY = 20
# Note: 'gemini-2.5-pro' is not a valid model as of now. Using the latest powerful model.
MODEL_NAME = "gemini-2.5-pro"


# New prompt for the on-demand detailed analysis page
detailed_analysis_prompt_template = """
You are a highly advanced video analysis AI. Your task is to perform a detailed analysis of the provided video based on the user's selected options.

**Instructions:**
{request_section}

Please format your response clearly using Markdown.
"""

# --- Session State Management ---
def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    state_defaults = {
        "history": [],
        "chat_history": [],
        "current_video_path": None,
        "current_video_name": "None",
        "processed_file": None,
        "detailed_analysis_result": None, # New state for the detailed analysis page
    }
    for key, value in state_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def initialize_chat():
    """Initialize chat with a welcome message if the history is empty."""
    if not st.session_state.chat_history:
        welcome_message = "Hello! I'm your Video Analysis Assistant. Upload a video and I'll help you analyze its content through our conversation!"
        st.session_state.chat_history.append({"role": "assistant", "content": welcome_message})

# --- Core Functions ---
def get_or_upload_video_file():
    """
    Uploads the video file to the Gemini API if not already processed.
    This is the key efficiency improvement: upload once, reuse many times.
    """
    if st.session_state.get("processed_file"):
        return st.session_state.processed_file

    if st.session_state.get("current_video_path"):
        with st.spinner('Preparing video for analysis... (this happens once per video)'):
            try:
                video_file = genai.upload_file(path=st.session_state.current_video_path)
                while video_file.state.name == "PROCESSING":
                    time.sleep(2)
                    video_file = genai.get_file(video_file.name)

                if video_file.state.name == "FAILED":
                    st.error("Video processing failed. Please try a different video.")
                    return None

                st.session_state.processed_file = video_file
                return video_file
            except Exception as e:
                logging.error(f"Error uploading/processing file: {e}")
                st.error(f"An error occurred during video preparation: {e}")
                return None
    return None

def get_detailed_analysis(video_file_api, generate_summary, generate_timeline):
    """
    Generates the detailed analysis based on user-selected checkboxes.
    """
    if not video_file_api:
        return "Error: Video file not available for analysis."
    if not generate_summary and not generate_timeline:
        return "Please select at least one analysis type to generate."

    request_section = ""
    if generate_summary:
        request_section += "1. **Generate a Detailed Summary:** Provide a comprehensive summary of the video. Include the main narrative, key events, the setting, mood, and any discernible purpose or message.\n"
    if generate_timeline:
        request_section += "2. **Generate an Object Timeline Table:** Create a Markdown table that lists prominent objects, people, or animals. The table must have two columns: 'Object/Person' and 'Timestamp of First Appearance'. The timestamp should be in MM:SS format.\n"

    final_prompt = detailed_analysis_prompt_template.format(request_section=request_section)

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(
            [final_prompt, video_file_api],
            request_options={'timeout': 600}
        )
        return response.text
    except Exception as e:
        logging.error(f"Error in detailed analysis: {e}")
        return f"Error: Could not generate detailed analysis. Details: {e}"

def handle_chat_input(chat_input, video_file_api):
    """Handles user chat input, generates a response, and updates history."""
    st.session_state.chat_history.append({"role": "user", "content": chat_input})

    with st.spinner('Thinking...'):
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            contents = [analysis_prompt, f"User Query: {chat_input} and Chat history: {st.session_state.chat_history}"]
            if video_file_api:
                contents.insert(1, video_file_api)
            else:
                contents[0] += "\nNote: The user has not uploaded a video. Please guide them to upload one if their query requires it."

            response = model.generate_content(contents)
            assistant_response = response.text
        except Exception as e:
            logging.error(f"Error during chat generation: {e}")
            assistant_response = f"Sorry, an error occurred: {e}"

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    if video_file_api:
        st.session_state.history.append({
            "query": chat_input,
            "response": assistant_response,
            "video_name": st.session_state.current_video_name,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

# --- Main Application UI ---
def main():
    st.set_page_config(
        page_title="Visual Understanding Chat Assistant",
        page_icon="🎥",
        layout="wide",
        initial_sidebar_state="auto"
    )
    st.title("🎥 Video Analysis Assistant")

    initialize_session_state()
    initialize_chat()

    with st.sidebar:
        st.header("Controls")
        mode = st.radio("Select Mode:", options=["Chat Mode", "Detailed Analysis", "Analysis History"], index=0)
        st.markdown("---")
        st.header("📹 Video Upload")
        video_file = st.file_uploader(
            "Upload your video",
            type=["mp4", "mov", "avi", "m4v"],
            help="Upload a video file for analysis."
        )

        if video_file:
            if video_file.name != st.session_state.current_video_name:
                st.session_state.current_video_name = video_file.name
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(video_file.name).suffix) as tfile:
                    tfile.write(video_file.read())
                    st.session_state.current_video_path = tfile.name
                
                # Reset all analysis results for the new video
                st.session_state.processed_file = None
                st.session_state.detailed_analysis_result = None
                st.success(f"✅ Loaded: {video_file.name}")
                st.rerun()

        if st.session_state.current_video_path:
            st.info(f"📹 Current video: **{st.session_state.current_video_name}**")
        else:
            st.info("Please upload a video to get started.")

    # --- Main Content Area ---
    video_file_api = get_or_upload_video_file() if st.session_state.current_video_path else None

    if mode == "Chat Mode":
        st.subheader("💬 Chat")
        if st.session_state.current_video_path:
            st.video(st.session_state.current_video_path)
        else:
            st.info("👆 Upload a video in the sidebar to start analyzing it through chat!")

        for message in st.session_state.chat_history[-NUMBER_OF_MESSAGES_TO_DISPLAY:]:
            role = message["role"]
            avatar = "🤖" if role == "assistant" else "👤"
            with st.chat_message(role, avatar=avatar):
                st.write(message["content"])

        if chat_input := st.chat_input("Ask anything about the video..."):
            handle_chat_input(chat_input, video_file_api)
            st.rerun()

    elif mode == "Detailed Analysis":
        st.subheader("🔬 Detailed Video Analysis")
        if video_file_api:
            st.video(st.session_state.current_video_path)
            st.markdown("---")
            st.markdown("##### Select analysis options and click Generate.")
            
            col1, col2 = st.columns(2)
            with col1:
                summary_cb = st.checkbox("Generate Detailed Summary", value=True)
            with col2:
                timeline_cb = st.checkbox("Generate Object Timeline Table", value=True)
            
            if st.button("Generate Detailed Analysis", type="primary"):
                with st.spinner("Performing detailed analysis... This may take a moment."):
                    result = get_detailed_analysis(video_file_api, summary_cb, timeline_cb)
                    st.session_state.detailed_analysis_result = result
            
            if st.session_state.detailed_analysis_result:
                st.markdown("---")
                st.markdown("### Analysis Result")
                st.markdown(st.session_state.detailed_analysis_result)

        else:
            st.info("👆 Please upload a video in the sidebar to perform a detailed analysis.")

    elif mode == "Analysis History":
        st.subheader("📊 Past Chat Analyses")
        if st.session_state.history:
            for i, entry in enumerate(reversed(st.session_state.history)):
                with st.expander(f"Analysis #{len(st.session_state.history)-i} - **{entry['video_name']}** ({entry['timestamp']})"):
                    st.markdown(f"**🗣️ You asked:**\n {entry['query']}")
                    st.markdown(f"**🤖 AI Responded:**\n {entry['response']}")
            
            if st.button("🗑️ Clear Chat History"):
                st.session_state.history = []
                st.rerun()
        else:
            st.info("No chat analysis history yet. Chat about a video to create a history entry.")

if __name__ == "__main__":
    main()