import os
import yaml
import subprocess
import platform

# Define the folder where your photos are stored
photos_folder = r"assets/gallery_pics"  # Use "/" for cross-platform compatibility
output_file = r"_data/photos.yaml"

# Function to open image with default viewer
def open_image(file_path):
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_path])
        else:  # Linux
            subprocess.run(["xdg-open", file_path])
    except Exception as e:
        print(f"Could not open image: {e}")

# Load existing photos data if file exists
existing_photos = {}
if os.path.exists(output_file):
    with open(output_file, "r") as f:
        existing_data = yaml.safe_load(f)
        if existing_data and "photos" in existing_data:
            for photo in existing_data["photos"]:
                # Use the filename as key for easy lookup
                filename = os.path.basename(photo["url"])
                existing_photos[filename] = photo["quote"]

# Initialize the YAML data structure
photos_data = []

# Iterate through files in the folder
for file_name in os.listdir(photos_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
        # Generate the photo path
        file_path = os.path.join(photos_folder, file_name)

        # Open the image in default viewer
        print(f"\nOpening image: {file_name}")
        open_image(file_path)

        # Check if this file already has a quote
        if file_name in existing_photos:
            current_quote = existing_photos[file_name]
            print(f"File: {file_name}")
            print(f"Current quote: {current_quote}")
            new_quote = input("Enter a new quote (or press Enter to keep current): ").strip()
            quote = new_quote if new_quote else current_quote
        else:
            print(f"File: {file_name}")
            print("Default quote: No quote chosen - Error 420")
            quote = input("Enter a quote: ").strip()
            quote = quote if quote else "No quote chosen - Error 420"

        # Add entry to the photos list
        photos_data.append({
            "description": "",
            "url": file_path,
            "quote": quote
        })

# Save to a YAML file
with open(output_file, "w") as f:
    yaml.dump({"photos": photos_data}, f, default_flow_style=False)

print(f"\nYAML file successfully saved as '{output_file}'!")
