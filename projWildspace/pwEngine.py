from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from npcGen import npc
from bldgGen import bldg
from twnGen import twn
from encGen import enc
from grpGen import grp
import os

class pwEngine:

    def __init__(self, ui, world):
        # Get API Key from .env file
        load_dotenv()
        self.token = os.environ.get("OPENAI_API_KEY")

        # Create Chat Model
        self.chat_llm = ChatOpenAI(openai_api_key=self.token)

        # Create Engines
        self.npc = npc(ui, self.chat_llm, world)
        self.bldg = bldg(ui, self.chat_llm, world)
        self.twn = twn(ui, self.chat_llm, world)
        self.enc = enc(ui, self.chat_llm, world)
        self.grp = grp(ui, self.chat_llm, world)

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

    def saveNPC(self):
        self.npc.save()
    
    def saveBLDG(self):
        self.bldg.save()

    def saveTWN(self):
        self.twn.save()

    def saveENC(self):
        self.enc.save()
    
    def saveGRP(self):
        self.grp.save()
    

