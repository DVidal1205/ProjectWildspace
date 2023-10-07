from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
import random
import math
import json
import os

# Create the PWEngine Class and Init method
class bldg:

    def __init__(self, ui, chat):
        # Create UI
        self.ui = ui

        # Create Chat Model
        self.chat_llm = chat

        # Schema
        # Building Generator
        # Owner Name
        # Building type (Tavern, Blacksmith, General Vendor, etc)
        # Building name
        # Architectural Style
        # Interior Environment / Ambience
        # Size
        # Foot Traffic
        # Entrance Description

        # Generate Schema
        self.type = ResponseSchema(name="type", description="Building Type (ex. Tavern, Blacksmith, Fisher, Market Vendor, etc)")
        self.name = ResponseSchema(name="name", description="Building Name. Be creative, and take inspiration from building type")
        self.architecture = ResponseSchema(name="architecture", description="Architectural Style (ex. Gothic, Modern, Steampunk, etc)")
        self.ambience = ResponseSchema(name="ambience", description="Description of the interior theme, style, and decor")
        self.size = ResponseSchema(name="size", description="Size of the building (ex. Small, Medium, Large, etc)")
        self.traffic = ResponseSchema(name="traffic", description="Amount of foot traffic the building receives (ex. Low, Medium, High, etc)")
        self.description = ResponseSchema(name="description", description="Description of what is going on in the building, and what the player sees when they enter (1-3 Sentences)")
        self.tender = ResponseSchema(name="tender", description="Building Tender Description. Include their name, race, and a brief description of their personality/appearance. (1-2 Sentences)")
        self.goods = ResponseSchema(name="goods", description="Description of the goods sold in the building. (1-2 Sentences)")
        self.response_schema = [self.type, self.name, self.architecture, self.ambience, self.size, self.traffic, self.description, self.tender, self.goods]

        # Create Schema Parser
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schema)
        self.format_instructions = self.output_parser.get_format_instructions()

        # Create Template
        self.template_string = """You are an expert Dungeon Master for Dungeons and Dragons Fifth Edition \ 
        You come up with catchy and memorable scenes and buildings for your D&D campaign.
        
        Create a concept for a place your party may stumble upon during their travels.

        For naming schemes, use prefixes from various languages to create names, or create combinations of words that sound cool together.

        When making this building/scence, be sure to contextualize the following information about the world as best as possible, i.e, include the world into your generation of the building.

        {world_info}   
        
        {format_instructions}"""

    def generate(self):

        # Create Prompt
        self.prompt = ChatPromptTemplate.from_template(template=self.template_string)

        # Create Messages
        self.messages = self.prompt.format_messages(format_instructions=self.format_instructions, world_info="World Name: Morellus. World Description: The nation of Morellus is a prosperous nation, but is severely oppressive towards those who use magic. Time Period: 1989 (Note: This is a fantasy world, so the time period is not the same as our own). Climate: Temperate. Presence of Magic: 8/10. Aesthetic: High Fantasy.")

        # Parse Response
        self.response = self.chat_llm(self.messages)
        self.response_as_dict = self.output_parser.parse(self.response.content)

        # Update Labels
        self.ui.buildingNameLabel.setText(self.response_as_dict["name"])
        self.ui.buildingTypeLabel.setText(self.response_as_dict["type"])
        self.ui.buildingTenderLabel.setText(self.response_as_dict["tender"])
        self.ui.buildingArcLabel.setText(self.response_as_dict["architecture"])
        self.ui.buildingAmbLabel.setText(self.response_as_dict["ambience"])
        self.ui.buildingSizeLabel.setText(self.response_as_dict["size"])
        self.ui.buildingTrafficLabel.setText(self.response_as_dict["traffic"])
        self.ui.buildingDesLabel.setText(self.response_as_dict["description"])
        self.ui.buildingGoodsLabel.setText(self.response_as_dict["goods"])

        


        
