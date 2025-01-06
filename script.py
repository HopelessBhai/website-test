import os
import yaml

# Define the folder where your photos are stored
photos_folder = "assets\\gallery_pics"
output_file = "photos.yaml"

# Initialize the YAML data structure
photos_data = []

# Iterate through files in the folder
for file_name in os.listdir(photos_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
        # Generate the photo URL (or path if not using URLs)
        file_path = os.path.join(photos_folder, file_name)
        photo_entry = {
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget risus nisi.",
            "url": file_path,
            "quote": "This is a quote 🐬"
        }
        photos_data.append(photo_entry)

# Save to a YAML file
with open(output_file, "w") as f:
    yaml.dump({"photos": photos_data}, f, default_flow_style=False)

print(f"YAML file generated: {output_file}")
