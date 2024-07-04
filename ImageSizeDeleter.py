# This deletes duplicate images regardless of size
# It also numerically sorts the animals after deleting some of the images

import os
from PIL import Image
import imagehash


def delete_duplicate_images(folder_path):
    # Dictionary to store image hash values
    hash_dict = {}

    # Loop through all images in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            try:
                image = Image.open(image_path)
                image_hash = imagehash.phash(image)

                # Check if the hash already exists
                if image_hash in hash_dict:
                    # If the hash exists, delete the duplicate image
                    print(f"Duplicate found: {filename} and {hash_dict[image_hash]}")
                    os.remove(image_path)
                else:
                    # If the hash does not exist, add it to the dictionary
                    hash_dict[image_hash] = filename
            except Exception as e:
                print(f"Error processing {filename}: {e}")


# Usage example
folder_path = (r"C:\Users\getan\GitHub\ML\Endangered_Images\Black-footed_Ferret")
delete_duplicate_images(folder_path)
animal_name = "Black-footed_Ferret"
import re


def rename_images_sequentially(folder_path, animal_name):
    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    # Sort the files based on the numerical part of the filename if present
    image_files.sort(key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)

    # Rename files sequentially
    for idx, filename in enumerate(image_files, start=1):
        # Extract the file extension
        file_extension = os.path.splitext(filename)[1]

        # Generate new filename
        new_filename = f"{animal_name}_{idx}{file_extension}"

        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

    print(f"Renamed {len(image_files)} images sequentially in '{folder_path}'.")


rename_images_sequentially(folder_path, animal_name)