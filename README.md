# 🛩 FlightAI - Airline Assistant

FlightAI is a chatbot for an airline, supporting both **OpenAI GPT (API)** and **Llama 3 (via Ollama, locally)**.

## 🔧 Features
- **Supports OpenAI GPT with function calling** (ticket prices lookup).
- **Supports Llama 3 locally via Ollama** (manual function execution).
- **Automatically detects available model and switches accordingly.**
- **Extensible and modular** for additional airline tools.

## 🎯 Objective
This implementation showcases the power of **Tools**, an incredibly powerful feature provided by frontier LLMs. Tools enable an LLM to call custom functions as part of its response, allowing for more dynamic and context-aware interactions. By integrating function calling, the assistant can:
- Fetch real-time ticket prices when requested.
- Extend its capabilities by calling additional airline-related functions.
- Provide more accurate responses by utilizing external data sources.

The implementation seamlessly supports OpenAI function calling and manually handles function execution for Llama-based models, demonstrating how different AI models can leverage structured function execution.

## 🚀 Setup Instructions

### **1. Clone the repository**
```sh
git clone https://github.com/yourusername/airline-assistant.git
cd airline-assistant
```

### **2. Install dependencies**
```sh
pip install -r requirements.txt
```

### **3. Configure environment variables**
Create a `.env` file (or copy `.env.example`) and add your OpenAI API key:
```sh
OPENAI_API_KEY=your_api_key_here
```

### **4. Run the chatbot**
```sh
python src/main.py
```

## 🛠 Tech Stack
- **Python** (3.9+)
- **OpenAI API** (for GPT models with function calling)
- **Ollama** (for Llama 3, locally, with manual function execution)
- **Gradio** (UI)

## 🤝 Contributing
Feel free to submit **issues** or **pull requests**! 🚀

