import os, json

def list_items():
    files = []
    for file in os.listdir("sample-skin"):
	    files.append(file)
    return files
 
items = list_items()

configs = 0
with open("config/config.json") as f:
    configs = json.load(f)

skins_folders = []
try:
    skins_folders = os.listdir(configs(f))
except:
    print("error with the skins folder")

randomized_skin = []
