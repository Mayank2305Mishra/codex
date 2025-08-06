# Codex: The Visual Understanding Chat Assistant 🎥🤖

[](https://www.python.org/)
[](https://streamlit.io)
[](https://ai.google.dev/)
[](https://opensource.org/licenses/MIT)

**A submission for the Mantra Hackathon - Round 1.**

Codex is an advanced, agentic chat assistant for visual understanding. It processes video input, recognizes key events, summarizes content, and engages in sophisticated multi-turn conversations with the user.
Collabrator :  MantraHackathon (https://github.com/MantraHackathon)
-----

## 🚀 Live Demo

Experience the power of Codex firsthand. Interact with the live application here:

**[https://codex-video-analyzer.streamlit.app/](https://codex-video-analyzer.streamlit.app/)**

-----

## ⚙️ Setup and Installation

Follow these instructions to get a local instance of Codex up and running.

**Prerequisites:**

  * Python 3.9+
  * Git

**1. Clone the Repository:**

```bash
git clone <your-repository-url>
cd <repository-directory>
```

**2. Create a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**4. Set Up Environment Variables:**

  * Create a file named `.env` in the root directory.
  * Add your Google AI API key to this file:

<!-- end list -->

```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

**5. Run the Application:**

```bash
streamlit run app.py
```

Your browser should automatically open to the application.

-----



## ✨ Features

Codex is built to deliver a seamless and intuitive video analysis experience. The core features implemented for Round 1 are:

  * [cite\_start]**🎬 Dynamic Video Processing:** Accepts and processes user-uploaded video streams (up to 2 minutes) in formats like MP4, MOV, and AVI. [cite: 19, 21]
  * **👁️ Event Recognition & Summarization:** Intelligently identifies key events, objects, and actions within the video. [cite\_start]It generates concise summaries, highlighting important moments and adherence to specific guidelines. [cite: 9, 10, 11]
  * **💬 Multi-Turn Conversational AI:** Powered by an agentic workflow, Codex supports natural, multi-turn conversations. [cite\_start]It retains context from previous interactions to answer follow-up questions coherently. [cite: 13, 14, 15, 16]
  * **🔬 Multiple Analysis Modes:**
      * **Chat Mode:** Engage in a real-time dialogue about the video content.
      * **Detailed Analysis:** Generate a comprehensive summary and a timestamped object timeline table.
      * **Analysis History:** Review and revisit past conversations and analyses.

-----

## 🏗️ System Architecture

The architecture is designed for simplicity, interactivity, and scalability, leveraging a powerful multimodal AI model at its core.

The workflow is as follows:

1.  **User Interface (Streamlit):** The user uploads a video and interacts with the assistant through a web-based interface.
2.  **Backend (Python/Streamlit):** The Streamlit server handles the application logic. It manages video file uploads, maintains session state, and orchestrates communication with the AI model.
3.  **Video Processing:** The uploaded video is temporarily stored and prepared for analysis.
4.  **AI Core (Google Gemini 1.5 Pro):** The video and user prompts (along with chat history for context) are sent to the Gemini API. The model performs the heavy lifting of visual understanding, event recognition, and response generation.
5.  **Response Delivery:** The generated text/analysis is streamed back to the backend and displayed to the user in the Streamlit UI.

-----

## 🛠️ Tech Stack & Justification

The technology stack was chosen to facilitate rapid development of a high-performance AI/ML application while ensuring scalability.

  * **Backend:** **Python**

      * **Justification:** Python is the undisputed leader in AI/ML development, offering an extensive ecosystem of libraries and frameworks. Its simplicity and power make it the ideal choice for building the application's logic.

  * **Frontend:** **Streamlit**

      * **Justification:** Streamlit is a premier open-source framework for building and sharing data and AI applications with minimal effort. [cite\_start]Its ability to create interactive UIs directly from Python scripts allowed for rapid prototyping and a focus on core functionality, which is perfect for this round's objectives. [cite: 4]

  * **AI Model:** **Google Gemini 1.5 Pro API**

      * [cite\_start]**Justification:** As a state-of-the-art, closed-source multimodal model, Gemini 1.5 Pro provides powerful, out-of-the-box capabilities for video understanding. [cite: 24] [cite\_start]Its large context window is excellent for multi-turn conversations, and its advanced reasoning allows for effective event recognition and summarization, perfectly aligning with the project's core requirements. [cite: 25]

-----


## 📖 Usage Instructions

Interacting with Codex is simple and intuitive.

**1. Upload a Video:**

  * Use the file uploader in the sidebar to select a video file (`.mp4`, `.mov`, etc.).
  * The application will process the video and display a success message.

**2. Chat Mode:**

  * This is the default mode.
  * The uploaded video will be displayed.
  * Type your questions into the chat input box at the bottom and press Enter.
  * **Example Query:** *"What is the main color of the car shown at the beginning?"* or *"Summarize the key events in this video."*

**3. Detailed Analysis Mode:**

  * Select "Detailed Analysis" from the sidebar.
  * Check the boxes for "Generate Detailed Summary" and/or "Generate Object Timeline Table".
  * Click the **"Generate Detailed Analysis"** button to receive a structured breakdown of the video content.

**4. Analysis History:**

  * Select "Analysis History" to view a log of your previous chat interactions for the current session.

-----

## 🎬 Demo Video

Below is a brief demonstration of the Codex assistant in action.
[![demo](https://img.shields.io/badge/DEMO_VIDEO-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://drive.google.com/file/d/1uZZ0brRgFM_-VYMv5mCAcn3UeTy1alEp/view?usp=sharing)
Direct Link : [https://drive.google.com/drive/my-drive](https://drive.google.com/file/d/1uZZ0brRgFM_-VYMv5mCAcn3UeTy1alEp/view?usp=sharing)



## Screenshots

#### Main App Layout
![App Screenshot](https://i.ibb.co/pqPBm50/Screenshot-2025-08-06-225509.png)

#### Response on the vidoe
![App Screenshot](https://i.ibb.co/VckfD9L2/Screenshot-2025-08-06-225532.png)

#### Summary 
![App Screenshot](https://i.ibb.co/RT1PZdKy/Screenshot-2025-08-06-225618.png)

#### Object Detection 
![App Screenshot](https://i.ibb.co/nN9jn32j/Screenshot-2025-08-06-225629.png)

#### History Overview
![App Screenshot](https://i.ibb.co/jkzdZ69f/Screenshot-2025-08-06-225657.png)


## 📩 Contact Info

## 🔗 Links (Mayank Mishra)
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://mayankmishra.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mayank-mishra-5884472b8/)
[![github](https://img.shields.io/badge/Github-1DA1F2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mayank2305Mishra)
#### Email : mayank2305mishra@gmail.com

