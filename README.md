# LangChain with Ollama - Streamlit Demo

A demonstration project using LangChain with Ollama's Llama 3.1 model, featuring a Streamlit web interface for interactive AI conversations.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+**
- **Ollama** - [Install from ollama.ai](https://ollama.ai)
- **Git** (optional, for version control)

## 🚀 Quick Start

### 1. Pull the Ollama Model

First, download and run the Llama 3.1 model (8B parameters):

```bash
ollama run llama3.1:8b
```

This command will:
- Download the model if not already present
- Start the Ollama server
- Load the model into memory

### 2. Verify Model is Running

Check that the model is active:

```bash
ollama ps
```

Expected output:
```
NAME           ID              SIZE      PROCESSOR    UNTIL
llama3.1:8b    46e0c10c039e    5.2 GB    100% GPU     4 minutes from now
```

### 3. Set Up Python Virtual Environment

Create and activate a Python 3.11 virtual environment:

```bash
# Create virtual environment
python3.11 -m venv myenv

# Activate virtual environment
source myenv/bin/activate
```

### 4. Verify Python Version

Confirm you're using Python 3.11:

```bash
python -V
```

Expected output:
```
Python 3.11.13
```

### 5. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 6. Run the Application

Launch the Streamlit application:

```bash
streamlit run ollamaDemo.py
```

The application will start and display:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8502
Network URL: http://192.168.29.242:8502
```

Open your browser and navigate to `http://localhost:8502` to interact with the application.

## 📦 Project Structure

```
langchain-ollama/
├── ollamaDemo.py          # Main Streamlit application
├── requirements.txt       # Python dependencies
├── myenv/                 # Virtual environment (not in git)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Example Screenshot from UI
<img width="1251" height="688" alt="Screenshot 2025-12-27 at 15 04 37" src="https://github.com/user-attachments/assets/6e185453-a4df-4938-b186-f702875f156b" />


