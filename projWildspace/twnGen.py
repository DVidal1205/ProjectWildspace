from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

# Create the PWEngine Class and Init method
class bldg:

    def __init__(self, ui, chat):
        # Create UI
        self.ui = ui

        # Create Chat Model
        self.chat_llm = chat

        # Generate Schema
        self.spawl = ResponseSchema(name="spawl", description="Sprawl Type (ex. Urban, Rural, etc)")
        self.name = ResponseSchema(name="name", description="Town Name. Be creative, and make the name sound fantasy by using prefixes from various languages")
        self.population = ResponseSchema(name="population", description="Number of citizens (25 to 100,000 inclusive)")
        self.architecture = ResponseSchema(name="architecture", description="Architectural Style (ex. Gothic, Modern, Steampunk, etc)")
        self.industries = ResponseSchema(name="industries", description="Main Industries (ex. Fishing, Mining, Farming, etc)")
        self.lore = ResponseSchema(name="lore", description="Town Lore (1-3 Sentences)") 
        self.governing = ResponseSchema(name="governing", description="Describe the governing body and political state of the town, and perhaps name it (1-3 Sentences)")
        self.quests = ResponseSchema(name="quests", description="Describe the quests that the party may find in the town (1-3 Sentences)")
        self.climate = ResponseSchema(name="climate", description="Climate (ex. Temperate, Tropical, etc)")
        self.response_schema = [self.spawl, self.name, self.population, self.architecture, self.industries, self.lore, self.governing, self.quests, self.climate]
        
        # Create Schema Parser
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schema)
        self.format_instructions = self.output_parser.get_format_instructions()

        # Create Template
        self.template_string = """You are an expert Dungeon Master for Dungeons and Dragons Fifth Edition \ 
        You come up with memorable and impactful towns/regions for your D&D campaign.
        
        Create a concept for a town or region that your party may stumble upon during their travels.

        When creating this town, be sure to include the following world information in your worldbuilding process.

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
