from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

# Create the PWEngine Class and Init method
class enc:

    def __init__(self, ui, chat):
        # Create UI
        self.ui = ui

        # Create Chat Model
        self.chat_llm = chat

        # Generate Schema
        self.description = ResponseSchema(name="description", description="Description of how the encounter begins, and some objectives for the encounter (1-3 Sentences)")
        self.creatures = ResponseSchema(name="creatures", description="A comma separated list of beasts from the 5e Monster Manual, based on the Challenge Ratings specified above")

        # Create Schema Parser
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schema)
        self.format_instructions = self.output_parser.get_format_instructions()

        # Create Template
        self.template_string = """You are an expert Dungeon Master for Dungeons and Dragons Fifth Edition \ 
        You come up with engaging and exciting combat encounters that your party may engage with.
        
        Create an encounter that your party may stumble upon during their travels.

        When creating this encounter, be sure to include the following world information in your worldbuilding process.

        {challenge_rating}

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
