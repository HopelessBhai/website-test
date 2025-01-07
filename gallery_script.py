import os
import yaml
from PIL import Image
import IPython.display as display

# Define the folder where your photos are stored
photos_folder = "assets/gallery_pics"  # Use "/" for cross-platform compatibility
output_file = "photos.yaml"

# Initialize the YAML data structure
photos_data = []

# Iterate through files in the folder
for file_name in os.listdir(photos_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
        # Generate the photo path
        file_path = os.path.join(photos_folder, file_name)

        # Display the image
        img = Image.open(file_path)
        display.display(img)

        # Prompt for user input
        print(f"File: {file_name}")
        description = ""
        quote = input("Enter a quote: ").strip()

        # Add entry to the photos list
        photos_data.append({
            "description": description,
            "url": file_path,
            "quote": quote or "Default quote."
        })

# Save to a YAML file
with open(output_file, "w") as f:
    yaml.dump({"photos": photos_data}, f, default_flow_style=False)

print(f"YAML file successfully saved as '{output_file}'!")
