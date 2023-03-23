import os
import json

def create_folders(data, parent_path):
    for key, value in data.items():
        current_path = os.path.join(parent_path, key)
        os.makedirs(current_path, exist_ok=True)

        # Create About.md file in the current folder
        with open(os.path.join(current_path, f"{key}.md"), "w") as about_file:
            about_file.write(f"# {key}\n\nThis is a brief description of {key}.\n")
        
        if isinstance(value, dict):
            create_folders(value, current_path)

with open("/Users/hiren/Documents/pravritti/knowledge_base/docs/Data/branches_of_education.json", "r") as file:
    branches_of_education = json.load(file)

create_folders(branches_of_education["Knowledge"], "Knowledge")