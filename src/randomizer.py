import os, json, random, shutil

def list_items():
    files = []
    for file in os.listdir("sample-skin"):
	    files.append(file)
    return files
 
items = list_items()

configs = 0
with open("config/config.json") as f:
    configs = json.load(f)

try:
    skins_folders = os.listdir(configs["skin_folder"])
except:
    print("error with the skins folder")

randomized_skin = []

while len(items) != 0:
    skin_path = configs["folder"] + '/' + random.choice(skins_folders) 
    skin_folder = os.listdir(skin_path)
    for file in skin_folder:
        if file == items[0]:
            shutil.copyfile(skin_path + '/' + file, "randomized_skin")
            items.remove(file)