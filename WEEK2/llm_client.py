
from abc import ABC, abstractmethod
from google import genai
import requests
import time

# Common interface
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# Gemini cloud provider

# Gemini cloud provider
class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        model = "gemini-3.8-flash"

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                return response.text

            except Exception as e:
                error = str(e)

                if any(code in error for code in ["503", "429", "500", "504"]):
                    if attempt < 2:
                        wait_time = 2 ** (attempt + 1)
                        print(f"\nGemini temporarily unavailable.")
                        print(f"Retrying in {wait_time} seconds...")
                        time.sleep(wait_time)
                    else:
                        print("\nGemini API is still unavailable.")
                        print("Please try again later or select Ollama.")
                        print("Error:", e)
                        return None
                else:
                    print("\nGemini API error:")
                    print(error)
                    return None

        return None


# Ollama local provider
class OllamaProvider(LLMProvider):

    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()
            return response.json()["response"]

        except requests.exceptions.RequestException as e:
            print("\nOllama is unavailable.")
            print("Error:", e)
            return None


# Common client
class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
