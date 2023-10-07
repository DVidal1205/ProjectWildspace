from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from npcGen import npc
from bldgGen import bldg
from twnGen import twn
from encGen import enc
from grpGen import grp
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
        self.bldg = bldg(ui, self.chat_llm)
        self.twn = twn(ui, self.chat_llm)
        self.enc = enc(ui, self.chat_llm)
        self.grp = grp(ui, self.chat_llm)

    def genNPC(self):
        self.npc.generate()

    def genBLDG(self):
        self.bldg.generate()

    def genTWN(self):    
        self.twn.generate()

    def genENC(self):
        self.enc.generate()

    def genGRP(self):
        self.grp.generate()

