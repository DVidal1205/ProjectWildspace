import os

class world:

    def __init__(self, ui):
        self.ui = ui

    def load(self):
        # Get the files in the worlds folder and add their names to the combobox
        folder_path = "saves/worlds"
        file_list = os.listdir(folder_path)
        text_files = [os.path.splitext(file.lower())[0] for file in file_list if file.lower().endswith('.txt')]
        
        # Clear to ensure no duplicates and then add the files
        self.ui.dropDown.clear()
        self.ui.dropDown.addItems(text_files)

    def loadWorld(self):
        self.worldName = self.ui.dropDown.currentText()
        self.filename = "saves/worlds/" + self.worldName + ".txt"
        self.file = open(self.filename, "r")
        contents = self.file.read()
        return contents


    def save(self):
        # Grab the world information
        self.world_name = self.ui.worldNameEdit.text()
        if self.world_name == None:
            return
        self.time_period = self.ui.worldTimeEdit.text()
        self.climate = self.ui.worldClimateEdit.text()
        self.geography = self.ui.worldGeoEdit.text()
        self.stability = self.ui.worldStabilityEdit.text()
        self.magic = self.ui.worldMagicEdit.text()
        self.theme = self.ui.worldThemeEdit.text()
        self.description = str(self.ui.worldDesEdit.toPlainText())

        # Create File
        self.filename = "saves/worlds/" + self.world_name.lower().replace(" ", "_") + ".txt"
        self.file = open(self.filename, "w")

        # Write to File
        self.file.write("World Name: " + self.world_name + "\n")
        self.file.write("World Time Period: " + self.time_period + "\n")
        self.file.write("World Climate: " + self.climate + "\n")
        self.file.write("World Geography: " + self.geography + "\n")
        self.file.write("World Stability: " + self.stability + "\n")
        self.file.write("World Magic: " + self.magic + "\n")
        self.file.write("World Theme: " + self.theme + "\n")
        self.file.write("World Description: " + self.description + "\n")

        # Close File
        self.file.close()
        
