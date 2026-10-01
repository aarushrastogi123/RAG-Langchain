import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
# print(os.getenv("GROQ_API_KEY"))


from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiLLM:
    def __init__(self, model_name: str = "gemini-2.5-flash", api_key: str = None):
        self.model_name = model_name
        self.api_key = api_key
        self.model = self.load_model()

    def load_model(self):
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set. Add it to the project-root .env file.")
        try:
            print(f'Loading Gemini model: {self.model_name}')
            model = ChatGoogleGenerativeAI(
                model=self.model_name,
                google_api_key=self.api_key,
                temperature=0.1,
                max_output_tokens=1024,
            )
            print('Gemini model loaded successfully')
            return model
        except Exception as e:
            print(f"Error loading Gemini model {self.model_name}: {e}")
            raise e
            
if __name__ == "__main__":
    # gemini_llm = GeminiLLM(api_key = gemini_api_key)
    print("ok")
