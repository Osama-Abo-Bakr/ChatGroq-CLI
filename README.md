# ChatGroq CLI - README

## Overview

**ChatGroq CLI** is a Python-based interactive chatbot application that leverages the power of the Groq AI model and LangChain's memory capabilities. It provides a conversational interface that remembers entities and context from the conversation to deliver more personalized and context-aware responses.

---

## Features

- **Powered by Groq AI:** Uses the `llama-3.3-70b-versatile` model for intelligent and versatile conversations.
- **Entity Memory:** Incorporates `ConversationEntityMemory` to remember key entities throughout the conversation.
- **Customizable Prompt Template:** Utilizes `ENTITY_MEMORY_CONVERSATION_TEMPLATE` for flexible prompt design.
- **Environment Variable Configuration:** API key management through a `.env` file for secure and convenient setup.

---

## Prerequisites

- Python 3.7 or higher
- `pip` for managing Python packages
- A valid Groq API key

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/ChatGroq-CLI.git
   cd ChatGroq-CLI
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=<your_groq_api_key>
   ```

---

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Interact with the chatbot by typing your queries in the console:
   ```plaintext
   > Hello, how are you?
   
   Assistant:
   I am an AI assistant, always ready to help. How can I assist you today?
   ```

---

## Code Explanation

### Main Components

1. **Environment Variable Loading:**
   - Uses `dotenv` to securely load the Groq API key from a `.env` file.

2. **Groq AI Model:**
   - Integrates the `ChatGroq` model for powerful conversational capabilities.

3. **Memory Integration:**
   - Utilizes `ConversationEntityMemory` from LangChain to remember entities across conversations, providing contextual continuity.

4. **Prompt Template:**
   - Implements `ENTITY_MEMORY_CONVERSATION_TEMPLATE` for flexible and structured conversations.

5. **Interactive CLI:**
   - A simple loop allows continuous interaction with the chatbot.

---

## Error Handling

- If the Groq API key is not set or is empty, the application will display an error message and terminate:
  ```plaintext
  Your Groq API key is not set. Please set it in the .env file.
  ```

---

## Dependencies

- `python-dotenv`
- `langchain`
- `langchain-groq`

Install these dependencies with:
```bash
pip install python-dotenv langchain langchain-groq
```

---

## Troubleshooting

- **Missing API Key:**
  Ensure the `.env` file is correctly configured with your Groq API key.

- **Dependency Issues:**
  Run `pip install -r requirements.txt` to install all necessary libraries.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any issues or feature requests, please create an issue in this repository or contact the maintainer.