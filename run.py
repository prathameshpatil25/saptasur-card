import os
import requests

# The base URL of the website
base_url = "https://saptasur.in"

# List of image paths extracted from the <img> tags in your code
image_paths = [
    "/static/new_featured/Rental.png",
    "/static/new_featured/Repair.png",
    "/static/new_featured/Studio.png",
    "/static//new_featured/Academy.png", # Handles the double slash
    "/static/new_featured/Showrrom.png"
]

def download_saptasur_images(output_folder="saptasur_images"):
    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    for path in image_paths:
        # Clean the path and create full URL
        clean_path = path.replace("//", "/")
        full_url = base_url + clean_path
        
        # Determine the local filename
        filename = os.path.join(output_folder, clean_path.split("/")[-1])

        try:
            print(f"Downloading: {full_url}...")
            response = requests.get(full_url, stream=True, timeout=10)
            
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Successfully saved to: {filename}")
            else:
                print(f"Failed to download. Status code: {response.status_code}")
        
        except Exception as e:
            print(f"An error occurred while downloading {full_url}: {e}")

if __name__ == "__main__":
    download_saptasur_images()