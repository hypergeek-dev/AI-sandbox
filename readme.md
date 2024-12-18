# AI Chatbot Sandbox

Welcome to the **AI Chatbot Sandbox**! This project is an experimental environment where I explore, build, and test AI-powered conversational agents using state-of-the-art models from the Hugging Face Transformers library.

## Project Overview

The goal of this sandbox is to:

1. Experiment with **pre-trained conversational models**, such as `facebook/blenderbot-400M-distill` and `facebook/opt-1.3b`.
2. Develop a chatbot capable of engaging in fluent, context-aware conversations.
3. Understand the mechanics of tokenization, context management, and response generation.
4. Explore different strategies for handling conversation history and improving user experience.

## Features

- **Conversational AI**: Implements conversational models to simulate human-like dialogue.
- **Customizable Context**: Maintains conversation history to provide context-aware responses.
- **Model Exploration**: Supports multiple pre-trained models to test performance and capabilities.
- **Real-Time Interaction**: Engage with the chatbot directly through a command-line interface (CLI).

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot-sandbox.git
   cd ai-chatbot-sandbox
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the chatbot using the following command:

```bash
python main.py
```

Once started, you can interact with the chatbot in a conversational loop. Type your messages, and the chatbot will respond. To exit the conversation, type `exit` or `quit`.
