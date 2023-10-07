from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
import os

# Create the PWEngine Class and Init method
class pwEngine:

    def __init__(self, ):
        # Get API Key from .env file
        load_dotenv()
        self.token = os.environ.get("OPENAI_API_KEY")

        # Create Chat Model
        self.chat_llm = ChatOpenAI(openai_api_key=self.token)