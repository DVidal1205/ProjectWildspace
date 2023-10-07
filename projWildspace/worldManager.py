import os, glob

class world:

    def __init__(self, ui):
        self.ui = ui

    def load(self):

        # Get the files in the worlds folder and add their names to the combobox
        folder_path = "/saves/worlds"
        file_list = os.listdir(folder_path)
        text_files = [os.path.splitext(file.lower())[0] for file in file_list if file.lower().endswith('.txt')]
        
        # Clear to ensure no duplicates and then add the files
        self.comboBox.clear()
        self.comboBox.addItems(text_files)

    def save(self):

        # Grab the world information
        self.world_name = self.ui.worldNameEdit.getText()
        self.time_period = self.ui.worldTimeEdit.getText()
        self.climate = self.ui.worldClimateEdit.getText()
        self.geography = self.ui.worldGeoEdit.getText()
        self.stability = self.ui.worldStabilityEdit.getText()
        self.magic = self.ui.worldMagicEdit.getText()
        self.theme = self.ui.worldThemeEdit.getText()
        self.description = str(self.ui.worldDesEdit.toPlainText())

        # Create File
        self.filename = "/saves/worlds" + self.world_name.lower().replace(" ", "_") + ".txt"
        self.file = open(self.filename, "w")

        # Write to File
        self.file.write("Name: " + self.world_name + "\n")
        self.file.write("Time Period: " + self.time_period + "\n")
        self.file.write("Climate: " + self.climate + "\n")
        self.file.write("Geography: " + self.geography + "\n")
        self.file.write("Stability: " + self.stability + "\n")
        self.file.write("Magic: " + self.magic + "\n")
        self.file.write("Theme: " + self.theme + "\n")
        self.file.write("Description: " + self.description + "\n")

        # Close File
        self.file.close()
        