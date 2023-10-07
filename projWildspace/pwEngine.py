from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from npcGen import npc
import os

# Create the PWEngine Class and Init method
class pwEngine:

    def __init__(self, ui):
        # Get API Key from .env file
        load_dotenv()
        self.token = os.environ.get("OPENAI_API_KEY")

        # Create Chat Model
        self.chat_llm = ChatOpenAI(openai_api_key=self.token)

        # Create Engines
        self.npc = npc(ui, self.chat_llm)

    def genNPC(self):
        self.npc.generate()

    def genBLDG(self):
        pass

    def genTWN(self):    
        pass

    def genENC(self):
        pass

    def genGRP(self):
        pass

