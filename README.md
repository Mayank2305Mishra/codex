# codex

# Visual Understanding Chat Assistant

Deployed Demo: https://codex-video-analyzer.streamlit.app/

---

### 📌 Project Overview
This project is a prototype for a **visual understanding chat assistant** that enables users to upload and analyze short video clips (up to 2 minutes). The assistant recognizes key events, detects guideline adherence (e.g., rule violations), generates textual summaries, and supports natural, multi-turn conversational exploration of the video content.

Use cases include traffic scene analysis, event annotation, and accessible video summarization. The assistant supports interactive, contextual conversations to let users query events, people, or rules detected in the video, all within a simple conversational interface.

---

### 🎯 Problem Statement Alignment
Round 1 Hackathon Goals & Features

| Requirement | Implemented in This Solution? | Description |
| :--- | :--- | :--- |
| Video Event Recognition & Summarization | ✅ | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence. |
| Multi-Turn Conversations | ✅ | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications. |
| Video Input Processing (≤2 min duration) | ✅ | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow. |
| Guideline Violation Reporting (e.g., traffic) | ✅ | Summarizes findings and can highlight rule or guideline violations when present and requested. |
| Agentic Workflow | ✅ | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

---

### 🏗️ Architecture Diagram
```text
                +-----------------+
                |    Frontend     |
          (Streamlit Web UI)
                +--------+--------+
                         |
              Video Upload, Chat Input/Output, Option Select
                         |
                +--------v--------+
                |    Backend      |
        (Streamlit, GenAI API)
                +--------+--------+
                         |
          +--------------v--------------+
          |       Gemini GenAI API      |
          +--------------+--------------+
                         |
         Video Event Recognition & Summarization
                         |
                +--------v--------+
                |  User receives  |
                |   Event Logs,   |
                |   Summaries,    |
                |  Timeline, Chat |
                +-----------------+
```

#### Flow:

    1. User uploads a video and enters queries via the web UI.

    2. Video is uploaded/staged to Google Gemini's API.

    3. Analysis prompts are sent for event detection, summary, and timeline creation.

    4. Responses (summaries, tables, reports) are formatted and rendered conversationally.

### ⚙️ Tech Stack Justification
##### Round 1 Hackathon Goals & Features

| **Requirement**                               | **Implemented in This Solution?** | **Description**                                                                                             |
|-----------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------|
| Video Event Recognition & Summarization       |                 ✅                 | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence.      |
| Multi-Turn Conversations                      |                 ✅                 | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications.  |
| Video Input Processing (≤2 min duration)      |                 ✅                 | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow.     |
| Guideline Violation Reporting (e.g., traffic) |                 ✅                 | Summarizes findings and can highlight rule or guideline violations when present and requested.              |
| Agentic Workflow                              |                 ✅                 | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

#### Suitability:

Using Streamlit and the Gemini API accelerates prototyping and experimentation, particularly for teams with limited on-premise GPU capacity. Google GenAI's video model does the heavy lifting, returning actionable insights and summaries in a manner that's easily orchestrated from Python.

# Visual Understanding Chat Assistant

Deployed Demo: https://codex-video-analyzer.streamlit.app/

---

### 📌 Project Overview
This project is a prototype for a **visual understanding chat assistant** that enables users to upload and analyze short video clips (up to 2 minutes). The assistant recognizes key events, detects guideline adherence (e.g., rule violations), generates textual summaries, and supports natural, multi-turn conversational exploration of the video content.

Use cases include traffic scene analysis, event annotation, and accessible video summarization. The assistant supports interactive, contextual conversations to let users query events, people, or rules detected in the video, all within a simple conversational interface.

---

### 🎯 Problem Statement Alignment
Round 1 Hackathon Goals & Features

| Requirement | Implemented in This Solution? | Description |
| :--- | :--- | :--- |
| Video Event Recognition & Summarization | ✅ | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence. |
| Multi-Turn Conversations | ✅ | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications. |
| Video Input Processing (≤2 min duration) | ✅ | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow. |
| Guideline Violation Reporting (e.g., traffic) | ✅ | Summarizes findings and can highlight rule or guideline violations when present and requested. |
| Agentic Workflow | ✅ | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

---

### 🏗️ Architecture Diagram
```text
                +-----------------+
                |    Frontend     |
          (Streamlit Web UI)
                +--------+--------+
                         |
              Video Upload, Chat Input/Output, Option Select
                         |
                +--------v--------+
                |    Backend      |
        (Streamlit, GenAI API)
                +--------+--------+
                         |
          +--------------v--------------+
          |       Gemini GenAI API      |
          +--------------+--------------+
                         |
         Video Event Recognition & Summarization
                         |
                +--------v--------+
                |  User receives  |
                |   Event Logs,   |
                |   Summaries,    |
                |  Timeline, Chat |
                +-----------------+
```

#### Flow:

    1. User uploads a video and enters queries via the web UI.

    2. Video is uploaded/staged to Google Gemini's API.

    3. Analysis prompts are sent for event detection, summary, and timeline creation.

    4. Responses (summaries, tables, reports) are formatted and rendered conversationally.

### ⚙️ Tech Stack Justification
##### Round 1 Hackathon Goals & Features

| **Requirement**                               | **Implemented in This Solution?** | **Description**                                                                                             |
|-----------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------|
| Video Event Recognition & Summarization       |                 ✅                 | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence.      |
| Multi-Turn Conversations                      |                 ✅                 | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications.  |
| Video Input Processing (≤2 min duration)      |                 ✅                 | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow.     |
| Guideline Violation Reporting (e.g., traffic) |                 ✅                 | Summarizes findings and can highlight rule or guideline violations when present and requested.              |
| Agentic Workflow                              |                 ✅                 | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

#### Suitability:

Using Streamlit and the Gemini API accelerates prototyping and experimentation, particularly for teams with limited on-premise GPU capacity. Google GenAI's video model does the heavy lifting, returning actionable insights and summaries in a manner that's easily orchestrated from Python.

# Visual Understanding Chat Assistant

Deployed Demo: https://codex-video-analyzer.streamlit.app/

---

### 📌 Project Overview
This project is a prototype for a **visual understanding chat assistant** that enables users to upload and analyze short video clips (up to 2 minutes). The assistant recognizes key events, detects guideline adherence (e.g., rule violations), generates textual summaries, and supports natural, multi-turn conversational exploration of the video content.

Use cases include traffic scene analysis, event annotation, and accessible video summarization. The assistant supports interactive, contextual conversations to let users query events, people, or rules detected in the video, all within a simple conversational interface.

---

### 🎯 Problem Statement Alignment
Round 1 Hackathon Goals & Features

| Requirement | Implemented in This Solution? | Description |
| :--- | :--- | :--- |
| Video Event Recognition & Summarization | ✅ | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence. |
| Multi-Turn Conversations | ✅ | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications. |
| Video Input Processing (≤2 min duration) | ✅ | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow. |
| Guideline Violation Reporting (e.g., traffic) | ✅ | Summarizes findings and can highlight rule or guideline violations when present and requested. |
| Agentic Workflow | ✅ | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

---

### 🏗️ Architecture Diagram
```text
                +-----------------+
                |    Frontend     |
          (Streamlit Web UI)
                +--------+--------+
                         |
              Video Upload, Chat Input/Output, Option Select
                         |
                +--------v--------+
                |    Backend      |
        (Streamlit, GenAI API)
                +--------+--------+
                         |
          +--------------v--------------+
          |       Gemini GenAI API      |
          +--------------+--------------+
                         |
         Video Event Recognition & Summarization
                         |
                +--------v--------+
                |  User receives  |
                |   Event Logs,   |
                |   Summaries,    |
                |  Timeline, Chat |
                +-----------------+
```

#### Flow:

    1. User uploads a video and enters queries via the web UI.

    2. Video is uploaded/staged to Google Gemini's API.

    3. Analysis prompts are sent for event detection, summary, and timeline creation.

    4. Responses (summaries, tables, reports) are formatted and rendered conversationally.

### ⚙️ Tech Stack Justification

| **Component** | **Choice**                                                     | **Why?**                                                                                       |
|---------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| UI            |                            Streamlit                           | Simple, fast, suitable for quick prototyping; user-friendly interface for both video and chat. |
| Backend       |       Python, Streamlit, Google Gemini API (google.genai)      | Python enables rapid integration with AI; Gemini API provides state-of-the-art video VLM.      |
| Video Proc    | Via Gemini's API & streaming through Streamlit and server-side | Offloads heavy ML workloads to cloud, simplifying implementation for limited compute locally.  |
| AI Models     |               Gemini 2.5 Pro (Google GenAI, API)               | Leading VLM for multimodal reasoning; excellent at video, text, and conversation tasks.        |
| State Mgmt    |                   Session state via Streamlit                  | Smooth multi-turn conversation with persistent context per user session. 

#### Suitability:

Using Streamlit and the Gemini API accelerates prototyping and experimentation, particularly for teams with limited on-premise GPU capacity. Google GenAI's video model does the heavy lifting, returning actionable insights and summaries in a manner that's easily orchestrated from Python.

---

## 📄 File Descriptions

| File / Directory     | Description |
|----------------------|-------------|
| **app.py**            | Main Streamlit application that runs the user interface and integrates backend functionalities. |
| **prompt.py**         | Stores reusable prompt templates like `analysis_prompt` for API interactions. |
| **.env**              | Environment configuration file that holds sensitive keys (e.g., API keys). **Do not commit this file to version control.** |
| **requirements.txt**  | Lists all Python packages and dependencies needed to run the application. |
| **README.md**         | Documentation file explaining the project structure and usage. |

---# Visual Understanding Chat Assistant

Deployed Demo: https://codex-video-analyzer.streamlit.app/

---

### 📌 Project Overview
This project is a prototype for a **visual understanding chat assistant** that enables users to upload and analyze short video clips (up to 2 minutes). The assistant recognizes key events, detects guideline adherence (e.g., rule violations), generates textual summaries, and supports natural, multi-turn conversational exploration of the video content.

Use cases include traffic scene analysis, event annotation, and accessible video summarization. The assistant supports interactive, contextual conversations to let users query events, people, or rules detected in the video, all within a simple conversational interface.

---

### 🎯 Problem Statement Alignment
Round 1 Hackathon Goals & Features

| Requirement | Implemented in This Solution? | Description |
| :--- | :--- | :--- |
| Video Event Recognition & Summarization | ✅ | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence. |
| Multi-Turn Conversations | ✅ | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications. |
| Video Input Processing (≤2 min duration) | ✅ | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow. |
| Guideline Violation Reporting (e.g., traffic) | ✅ | Summarizes findings and can highlight rule or guideline violations when present and requested. |
| Agentic Workflow | ✅ | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

---

### 🏗️ Architecture Diagram
```text
                +-----------------+
                |    Frontend     |
          (Streamlit Web UI)
                +--------+--------+
                         |
              Video Upload, Chat Input/Output, Option Select
                         |
                +--------v--------+
                |    Backend      |
        (Streamlit, GenAI API)
                +--------+--------+
                         |
          +--------------v--------------+
          |       Gemini GenAI API      |
          +--------------+--------------+
                         |
         Video Event Recognition & Summarization
                         |
                +--------v--------+
                |  User receives  |
                |   Event Logs,   |
                |   Summaries,    |
                |  Timeline, Chat |
                +-----------------+
```

#### Flow:

    1. User uploads a video and enters queries via the web UI.

    2. Video is uploaded/staged to Google Gemini's API.

    3. Analysis prompts are sent for event detection, summary, and timeline creation.

    4. Responses (summaries, tables, reports) are formatted and rendered conversationally.

### ⚙️ Tech Stack Justification
##### Round 1 Hackathon Goals & Features

| **Requirement**                               | **Implemented in This Solution?** | **Description**                                                                                             |
|-----------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------|
| Video Event Recognition & Summarization       |                 ✅                 | Detects, summarizes, and reports key events and objects from video input; reports guideline adherence.      |
| Multi-Turn Conversations                      |                 ✅                 | Chatbot remembers conversation history and context for coherent, follow-up discussions and clarifications.  |
| Video Input Processing (≤2 min duration)      |                 ✅                 | Accepts, uploads, and processes video files up to 2 minutes, with efficient handling and user workflow.     |
| Guideline Violation Reporting (e.g., traffic) |                 ✅                 | Summarizes findings and can highlight rule or guideline violations when present and requested.              |
| Agentic Workflow                              |                 ✅                 | Allows sequential and contextual interaction, supports different query types for detailed analysis or chat. |

#### Suitability:

Using Streamlit and the Gemini API accelerates prototyping and experimentation, particularly for teams with limited on-premise GPU capacity. Google GenAI's video model does the heavy lifting, returning actionable insights and summaries in a manner that's easily orchestrated from Python.

