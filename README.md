# 👻 GhostWriter AI — Local AI-Powered Spooky Story Generator

GhostWriter AI is a Python-based web application that generates spooky and horror-themed stories using a locally running AI model through Ollama. The application provides a simple Streamlit interface where users can generate stories, choose a theme and length, and save generated stories in a local story library.

This project explores how open-weight AI models can be used locally to create fictional content without relying on a cloud-based AI API for story generation.

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation and Setup](#-installation-and-setup)
- [Running the Application](#-running-the-application)
- [Testing the Application](#-testing-the-application)
- [Privacy and Data Storage](#-privacy-and-data-storage)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

---

## 📖 About the Project

GhostWriter AI is a local AI-powered story generator designed for users who enjoy horror, ghost stories, haunted locations, and mysterious fictional narratives.

Users can choose a story theme and preferred length, then generate a story using an AI model running locally through Ollama.

The application also includes a Story Library that allows users to save generated stories and view them later.

The project was built as a learning project to explore Python development, Streamlit web applications, local AI model integration, and JSON-based data storage.

---

## ✨ Features

### 👻 AI Story Generation

Generate fictional spooky stories using an AI model connected through Ollama.

### 🎭 Theme Selection

Choose an available theme from the application's theme selector. The current interface includes a Ghost Story option.

### 📏 Story Length Selection

Choose a preferred story length. The current interface includes a short option of approximately 150 words.

### 📚 Story Library

Save generated stories and view previously saved entries through the Story Library interface.

### 💾 Local JSON Storage

Saved story information is stored in a local JSON file.

### 🌙 Simple Web Interface

The application uses Streamlit to provide an interactive web interface without requiring a separate frontend framework.

### 🖥️ Local AI Integration

The application is designed to connect to Ollama and use a locally available AI model for story generation.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| Ollama | Local AI model runtime |
| Qwen2.5 0.5B | AI model tested during development |
| JSON | Local storage for saved stories |
| Git | Version control |
| GitHub | Source code hosting |

**Model note:** The model used during development was `qwen2.5:0.5b`. The model must be available in the local Ollama installation for the application to use it.

---

## ⚙️ How It Works

1. The user opens the GhostWriter AI web application.
2. The user selects an available story theme and preferred story length.
3. The user clicks the Generate Story button.
4. The application prepares a prompt and sends it to the configured local AI model through Ollama.
5. The model generates fictional story content.
6. The application displays the generated story.
7. The user can save the story to the Story Library.
8. Saved story data is written to a local JSON file and loaded when the library is displayed.

---

## 📁 Project Structure

```text
GhostWriterAI/
│
├── app.py
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── stories.json
│
└── .venv/
```

### File Descriptions

- `app.py` — Contains the main Streamlit application, story generation logic, and Story Library functionality.
- `README.md` — Project documentation.
- `requirements.txt` — Python dependencies required to run the application.
- `.gitignore` — Specifies files and folders that Git should ignore.
- `data/stories.json` — Stores saved stories locally when the application uses this file.
- `.venv/` — Local Python virtual environment. This folder should not be committed to GitHub.

The `.venv/` folder is shown for documentation purposes only and should be excluded from the repository.

---

## 📋 Requirements

Before running GhostWriter AI, make sure you have:

- Python installed.
- Git installed if you want to clone or contribute to the repository.
- Ollama installed and running.
- A compatible model downloaded in Ollama.
- The Python packages listed in `requirements.txt`.

The model used during development was:

```text
qwen2.5:0.5b
```

---

## 🚀 Installation and Setup

### 1. Clone the Repository

Replace `YOUR_USERNAME` with the GitHub account that owns the repository.

```bash
git clone https://github.com/YOUR_USERNAME/GhostWriterAI.git
cd GhostWriterAI
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

### 3. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, follow the Python environment activation instructions appropriate for your Windows configuration.

### 4. Install Python Dependencies

Install the packages recorded in `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

If the repository does not yet contain `requirements.txt`, create it from the packages actually used by the application before following this step.

### 5. Install and Start Ollama

Install Ollama from its official website:

https://ollama.com/

Make sure Ollama is running.

Download the model used during development:

```powershell
ollama pull qwen2.5:0.5b
```

Verify that the model is available:

```powershell
ollama list
```

The model list should include `qwen2.5:0.5b`.

---

## ▶️ Running the Application

From the project directory, activate the virtual environment and run:

```powershell
streamlit run app.py
```

Streamlit will display a local URL in the terminal, usually:

```text
http://localhost:8501
```

Open the displayed local URL in your browser.

Keep the terminal and Ollama running while using the application.

---

## 🧪 Testing the Application

The following checks can be performed to verify the application.

### Test 1: Generate a Story

1. Open the application.
2. Choose an available theme.
3. Choose a story length.
4. Click Generate Story.
5. Verify that the generated content appears.

### Test 2: Save a Story

1. Generate a story.
2. Click Save to Story Library.
3. Verify that a success message appears.
4. Confirm that the saved story is displayed in the library.

### Test 3: Save Multiple Stories

1. Generate and save a story with one topic.
2. Generate and save another story with a different topic.
3. Check whether both stories appear in the Story Library.

### Test 4: Refresh the Application

1. Save one or more stories.
2. Refresh the browser.
3. Check whether the saved stories are loaded again.

### Test 5: Verify Local Model Availability

Run:

```powershell
ollama list
```

Confirm that the configured model is available before testing story generation.

These are recommended verification steps. Results may vary depending on the local environment, model configuration, and application implementation.

---

## 🔐 Privacy and Data Storage

GhostWriter AI is designed to use a locally running Ollama model for story generation.

Saved story data is stored locally in a JSON file when the application uses the default local storage configuration.

Important considerations:

- Do not commit API keys, passwords, or other secrets to the repository.
- Do not upload personal stories or sensitive data unintentionally.
- Keep `.env` files and private configuration files out of Git.
- Exclude the `.venv/` folder from version control.
- Review application configuration before using sensitive information.

Local model execution reduces dependence on cloud-based AI APIs, but privacy also depends on the application's configuration and the other services it uses.

---

## ⚠️ Limitations

- Story quality depends on the selected model and prompt.
- Generated stories may contain inconsistencies or repetitive content.
- A compatible local Ollama installation is required.
- AI generation speed depends on the computer's hardware and the selected model.
- Saved stories depend on the configured local storage file.
- The current project is a learning prototype and may require further testing before broader use.

---

## 🔮 Future Improvements

Possible future enhancements include:

- More story themes and genres.
- Custom story length and writing style controls.
- Search and filtering for saved stories.
- Story deletion and editing.
- Export stories to additional file formats.
- Improved error handling and Ollama connection status.
- A more responsive and customizable interface.
- Automated tests for story generation and saving.
- Optional database support for larger story collections.

These are planned improvements and may not be available in the current version.

---

## 🎓 Learning Outcomes

This project provides practical experience with:

- Python application development.
- Building interactive interfaces with Streamlit.
- Connecting an application to a local AI model through Ollama.
- Prompt-based AI text generation.
- Saving and loading data using JSON.
- Managing a Python virtual environment.
- Using Git and GitHub for version control and project sharing.

---

## 👨‍💻 Author

Created as a learning project exploring local AI, open-weight models, and Python application development.

**Project:** GhostWriter AI  
**Category:** Local AI / Generative AI  
**Language:** Python

---

## 📄 License

No license has been selected for this repository yet. If you want others to reuse, modify, or distribute the code, consider adding an appropriate open-source license.
