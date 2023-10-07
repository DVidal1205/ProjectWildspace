from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

# Create the PWEngine Class and Init method
class grp:

    def __init__(self, ui, chat):
        # Create UI
        self.ui = ui

        # Create Chat Model
        self.chat_llm = chat

        # Generate Schema
        self.name = ResponseSchema(name="name", description="Faction Name. Be creative, and make the name sound fantasy by using prefixes from various languages")
        self.goal = ResponseSchema(name="goal", description="Common goal / cause of the faction (1-3 Sentences)")
        self.features = ResponseSchema(name="features", description="Identifying features of the faction, such as symbols, clothing, phrases, etc (1-3 Sentences)")
        self.morality = ResponseSchema(name="morality", description="Morality of the faction. Use D&D Alignments as responses")
        self.activities = ResponseSchema(name="activities", description="Activities / Presence of the faction (1-3 Sentences)")
        self.devotion = ResponseSchema(name="devotion", description="Level of devotion to the faction (ex. Low, Medium, High, Fanatic, etc)")
        self.sentiment = ResponseSchema(name="sentiment", description="Sentiment towards outsiders (ex. Friendly, Neutral, Hostile, etc)")
        self.response_schema = [self.name, self.goal, self.features, self.morality, self.activities, self.devotion, self.sentiment]

        # Create Schema Parser
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schema)
        self.format_instructions = self.output_parser.get_format_instructions()

        # Create Template
        self.template_string = """You are an expert Dungeon Master for Dungeons and Dragons Fifth Edition \ 
        You come up with memorable and impactful groups and factions that your party may interact with.
        
        Create a group or faction that your party may stumble upon during their travels.

        When creating this group or faction, be sure to include the following world information in your worldbuilding process.

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
