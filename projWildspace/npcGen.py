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
class npc:

    def __init__(self, ui, chat):
        # Create UI
        self.ui = ui

        # Create Chat Model
        self.chat_llm = chat

        self.race_info = [
                {"Race": "Aarakockra", "Low Age": 3, "High Age": 30, "Low Height": 60, "High Height": 72},
                {"Race": "Aasimar", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Bugbear", "Low Age": 16, "High Age": 80, "Low Height": 72, "High Height": 96},
                {"Race": "Centaur", "Low Age": 15, "High Age": 100, "Low Height": 72, "High Height": 84},
                {"Race": "Changeling", "Low Age": 20, "High Age": 80, "Low Height": 60, "High Height": 72},
                {"Race": "Dragonborn", "Low Age": 15, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Chromatic Dragonborn", "Low Age": 15, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Gem Dragonborn", "Low Age": 15, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Metallic Dragonborn", "Low Age": 15, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Dwarves", "Low Age": 50, "High Age": 350, "Low Height": 36, "High Height": 48},
                {"Race": "Duergar", "Low Age": 50, "High Age": 350, "Low Height": 36, "High Height": 48},
                {"Race": "Hill Dwarf", "Low Age": 50, "High Age": 350, "Low Height": 36, "High Height": 48},
                {"Race": "Mountain Dwarf", "Low Age": 50, "High Age": 350, "Low Height": 36, "High Height": 48},
                {"Race": "Elves", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Astral Elf", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Drow (Dark Elf)", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Eladrin", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "High Elf", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Sea Elf", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Shadar-Kai", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Wood Elf", "Low Age": 100, "High Age": 750, "Low Height": 60, "High Height": 72},
                {"Race": "Fairy", "Low Age": 20, "High Age": 200, "Low Height": 48, "High Height": 72},
                {"Race": "Firbolg", "Low Age": 30, "High Age": 500, "Low Height": 72, "High Height": 96},
                {"Race": "Genasi", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Air Genasi", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Earth Genasi", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Fire Genasi", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Water Genasi", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Giff", "Low Age": 18, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Gith", "Low Age": 18, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Githyanki", "Low Age": 18, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Githzerai", "Low Age": 18, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Gnomes", "Low Age": 20, "High Age": 500, "Low Height": 36, "High Height": 48},
                {"Race": "Autognome", "Low Age": 20, "High Age": 500, "Low Height": 36, "High Height": 48},
                {"Race": "Deep Gnome (Svirfneblin)", "Low Age": 20, "High Age": 500, "Low Height": 36, "High Height": 48},
                {"Race": "Forest Gnome", "Low Age": 20, "High Age": 500, "Low Height": 36, "High Height": 48},
                {"Race": "Rock Gnome", "Low Age": 20, "High Age": 500, "Low Height": 36, "High Height": 48},
                {"Race": "Goblin", "Low Age": 10, "High Age": 60, "Low Height": 36, "High Height": 48},
                {"Race": "Goliath", "Low Age": 18, "High Age": 100, "Low Height": 72, "High Height": 96},
                {"Race": "Grung", "Low Age": 18, "High Age": 80, "Low Height": 24, "High Height": 48},
                {"Race": "Hadozee", "Low Age": 15, "High Age": 60, "Low Height": 60, "High Height": 84},
                {"Race": "Half-Elf", "Low Age": 20, "High Age": 180, "Low Height": 60, "High Height": 72},
                {"Race": "Half-Orc", "Low Age": 14, "High Age": 75, "Low Height": 60, "High Height": 84},
                {"Race": "Halflings", "Low Age": 20, "High Age": 250, "Low Height": 24, "High Height": 36},
                {"Race": "Ghostwise Halfling", "Low Age": 20, "High Age": 250, "Low Height": 24, "High Height": 36},
                {"Race": "Lightfoot Halfling", "Low Age": 20, "High Age": 250, "Low Height": 24, "High Height": 36},
                {"Race": "Stout Halfling", "Low Age": 20, "High Age": 250, "Low Height": 24, "High Height": 36},
                {"Race": "Harengon", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Hobgoblin", "Low Age": 20, "High Age": 80, "Low Height": 60, "High Height": 72},
                {"Race": "Human", "Low Age": 18, "High Age": 100, "Low Height": 48, "High Height": 84},
                {"Race": "Kalashtar", "Low Age": 20, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Kender", "Low Age": 20, "High Age": 100, "Low Height": 36, "High Height": 48},
                {"Race": "Kenku", "Low Age": 12, "High Age": 60, "Low Height": 48, "High Height": 60},
                {"Race": "Kobold", "Low Age": 6, "High Age": 120, "Low Height": 24, "High Height": 36},
                {"Race": "Leonin", "Low Age": 18, "High Age": 100, "Low Height": 72, "High Height": 84},
                {"Race": "Lizardfolk", "Low Age": 14, "High Age": 60, "Low Height": 60, "High Height": 84},
                {"Race": "Locathah", "Low Age": 10, "High Age": 80, "Low Height": 48, "High Height": 72},
                {"Race": "Loxodon", "Low Age": 50, "High Age": 450, "Low Height": 72, "High Height": 96},
                {"Race": "Minotaur", "Low Age": 20, "High Age": 150, "Low Height": 72, "High Height": 84},
                {"Race": "Orc", "Low Age": 12, "High Age": 80, "Low Height": 60, "High Height": 84},
                {"Race": "Owlin", "Low Age": 15, "High Age": 80, "Low Height": 60, "High Height": 72},
                {"Race": "Plasmoids", "Low Age": 10, "High Age": 100, "Low Height": 48, "High Height": 72},
                {"Race": "Satyr", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Shifter", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Simic Hybrid", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Tabaxi", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Thri-Kreen", "Low Age": 5, "High Age": 30, "Low Height": 72, "High Height": 84},
                {"Race": "Tiefling", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Tortle", "Low Age": 15, "High Age": 60, "Low Height": 48, "High Height": 60},
                {"Race": "Triton", "Low Age": 18, "High Age": 200, "Low Height": 60, "High Height": 72},
                {"Race": "Vedalken", "Low Age": 20, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Verdan", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
                {"Race": "Warforged", "Low Age": 2, "High Age": 30, "Low Height": 60, "High Height": 84},
                {"Race": "Yuan-Ti Pureblood", "Low Age": 18, "High Age": 100, "Low Height": 60, "High Height": 72},
        ]
        self.hairColors = ["Black", "Brown", "Dark Brown", "Light Brown", "Golden Brown", "Chestnut Brown",
        "Auburn", "Red", "Strawberry Blonde", "Blonde", "Platinum Blonde", "Dirty Blonde",
        "Ash Blonde", "Honey Blonde", "Sandy Blonde", "Silver", "Gray", "Salt and Pepper",
        "White", "Blue", "Navy Blue", "Teal", "Green", "Emerald Green", "Forest Green",
        "Olive Green", "Mint Green", "Pink", "Hot Pink", "Bubblegum Pink", "Lavender",
        "Purple", "Violet", "Indigo", "Lilac", "Orchid", "Orchid Pink", "Peach", "Copper",
        "Mahogany", "Burgundy", "Maroon", "Wine", "Rust", "Cinnamon", "Amber", "Honey",
        "Tawny", "Platinum", "Lavender Gray", "Steel Gray", "Charcoal", "Rainbow", "Ombre",
        "Two-Tone", "Highlights", "Lowlights", "Balayage", "Unicorn", "Mermaid", "Neon",
        "Pastel", "Iridescent", "Opal", "Silver Fox", "Natural"]
        self.eyeColors = [
        "Amber", "Blue", "Brown", "Green", "Gray", "Hazel", "Black", "Red", "Violet",
        "Aqua", "Teal", "Turquoise", "Gold", "Silver", "Copper", "Topaz", "Emerald",
        "Sapphire", "Ruby", "Opal", "Onyx", "Peridot", "Aquamarine", "Jade", "Bronze",
        "Chestnut", "Olive", "Lavender", "Indigo", "Honey", "Pink", "Platinum", "White",
        "Mixed", "Multicolored", "Other"]
        self.builds = [
        "Muscular", "Skinny", "Cunning", "Bulky", "Lean", "Athletic",
        "Tall", "Short", "Average", "Stocky", "Chubby", "Slender", "Hulking",
        "Compact", "Stout", "Lithe", "Robust", "Gangly", "Toned", "Gnarled"]
        self.genderList = ["Male", "Female", "Non-Binary", "Construct"]
        
        # Generate Schema
        self.first_name_schema = ResponseSchema(name="first_name", description="Character first name")
        self.last_name_schema = ResponseSchema(name="last_name", description="Character last name")
        self.background_schema = ResponseSchema(name="background", description="Character Lore/Background (1-3 sentences))")
        self.motivation_schema = ResponseSchema(name="motivation", description="Character Motivation (1-3 sentences)")
        self.quirk_schema = ResponseSchema(name="quirk", description="Character Roleplay Quirk (1-3 sentences)")
        self.fashion_schema = ResponseSchema(name="fashion", description="Fashion Style (1-3 sentences)")        
        self.response_schema = [self.first_name_schema, self.last_name_schema, self.background_schema, self.motivation_schema, self.quirk_schema, self.fashion_schema]

        # Create Schema Parser
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schema)
        self.format_instructions = self.output_parser.get_format_instructions()

        # Create Template
        self.template_string = """You are an expert Dungeon Master for Dungeons and Dragons Fifth Edition \ 
        You come up with catchy and memorable ideas for a Dungeons and Dragons Campaign.
        
        Create a character concept for an NPC your party may encounter using the following information.

        For naming schemes, use prefixes from various languages to create names.

        When making this character, be sure to contextualize the following information about the world as best as possible, i.e, include the world into your generation of the character.

        {character_info}

        {world_info}   
        
        {format_instructions}"""

    def generate(self):

        # Create Empty Dict
        self.character_traits = {}

        # Create Prompt
        self.prompt = ChatPromptTemplate.from_template(template=self.template_string)

        # Gather Race

        self.racial = random.choice(self.race_info)
        self.character_traits["race"] = self.racial["Race"]

        # Age
        self.lowAge = int(self.racial["Low Age"])
        self.highAge = int(self.racial["High Age"])
        self.age = str(random.randint(self.lowAge, self.highAge))
        self.character_traits["age"] = self.age

        # Height
        self.lowHeight = int(self.racial["Low Height"])
        self.highHeight = int(self.racial["High Height"])
        self.height = random.randint(self.lowHeight, self.highHeight)
        self.heightFt = math.floor(self.height/12)
        self.heightIn = self.height % 12
        self.finalHeight = str(self.heightFt) + "'" + str(self.heightIn) + "\""
        self.character_traits["height"] = self.finalHeight

        # Hair
        self.hair = random.choice(self.hairColors)
        self.character_traits["hair"] = self.hair

        # Eyes
        self.eyes = random.choice(self.eyeColors)
        self.character_traits["eyes"] = self.eyes

        # Build
        self.build = random.choice(self.builds)
        self.character_traits["build"] = self.build

        # Gender
        self.gender = random.choice(self.genderList)
        self.character_traits["gender"] = self.gender

        # Create Messages
        self.messages = self.prompt.format_messages(format_instructions=self.format_instructions, character_info=self.character_traits, world_info="World Name: Morellus. World Description: The nation of Morellus is a prosperous nation, but is severely oppressive towards those who use magic. Time Period: 1989 (Note: This is a fantasy world, so the time period is not the same as our own). Climate: Temperate. Presence of Magic: 8/10. Aesthetic: High Fantasy.")

        # Parse Response
        self.response = self.chat_llm(self.messages)
        self.response_as_dict = self.output_parser.parse(self.response.content)

        # Add to character traits
        self.character_traits["first_name"] = self.response_as_dict["first_name"]
        self.character_traits["last_name"] = self.response_as_dict["last_name"]
        self.character_traits["background"] = self.response_as_dict["background"]
        self.character_traits["motivation"] = self.response_as_dict["motivation"]
        self.character_traits["quirk"] = self.response_as_dict["quirk"]
        self.character_traits["fashion"] = self.response_as_dict["fashion"]

        # Print
        self.json_object = json.dumps(self.character_traits, indent = 4)
        self.ui.label.setText(self.json_object)


        
