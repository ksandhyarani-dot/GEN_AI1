# Week 2 – Multiple LLM Provider Integration

## Project Description

This project demonstrates how to integrate multiple Large Language Model (LLM) providers using Python. It allows users to interact with either Google's Gemini AI or the locally running Ollama model through a common interface.

The main objective is to understand how different AI providers can be connected and used within a single Python application.

## Files Description

### 1. main.py
- Acts as the main entry point of the application.
- Allows the user to select an AI provider (Gemini or Ollama).
- Accepts a question or prompt from the user.
- Sends the prompt to the selected LLM provider.
- Displays the generated AI response.

### 2. llm_client.py
- Contains the implementation of multiple LLM providers.
- Defines an abstract base class called `LLMProvider`.
- Implements `GeminiProvider` to connect with Google's Gemini API.
- Implements `OllamaProvider` to connect with the locally running Ollama model.
- Uses the `LLMClient` class to provide a common interface for both providers.
- Includes error handling and retry mechanisms for temporary Gemini API failures.

### 3. requirements.txt
- Contains the Python libraries required for the project.
- Helps install the dependencies needed to run the application.

## Technologies Used

- Python
- Google Gemini API
- Ollama
- Object-Oriented Programming (OOP)
- Abstract Base Classes (ABC)
- Requests Library

## Installation

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Execute the main Python file:

```bash
python main.py
```

Choose the provider:

```text
Choose provider (gemini/ollama):
```

Enter `gemini` to use Google's Gemini AI or `ollama` to use the locally installed Ollama model.

Then enter your question to receive an AI-generated response.

## Sample Output

```text
Choose provider (gemini/ollama): gemini
Enter your question: what is linux

AI Response:
Linux is a free and open-source operating system...
```

## Learning Outcomes

- Understanding Large Language Models (LLMs).
- Integrating Gemini API with Python.
- Running local AI models using Ollama.
- Applying abstraction and inheritance in Python.
- Understanding how to design a common interface for multiple AI providers.
- Handling API errors and exceptions.

## Conclusion

This project demonstrates how multiple AI providers can be integrated into one Python application using object-oriented programming principles. It provides flexibility to switch between cloud-based Gemini AI and locally running Ollama models.
