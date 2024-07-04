# custom single search engine

import os
import requests
from googleapiclient.discovery import build

# Google API key and Custom Search Engine ID
API_KEY = 'AIzaSyAAZh0Gj7FLtkGsC_EkBwrAqqSubRNKzeQ'
CSE_ID = '3048a6d7aa0fe4939'

def get_animal_images_google(animal_name, save_root_dir, max_images=200):
    # Create directory path for the current animal
    animal_dir = os.path.join(save_root_dir, animal_name.replace(' ', '_'))

    # Ensure directory exists or create it
    if not os.path.exists(animal_dir):
        os.makedirs(animal_dir)

    # Find the number of existing images
    existing_images = len(os.listdir(animal_dir))

    additional_images_needed = max_images - existing_images
    if additional_images_needed <= 0:
        print(f"Already have {max_images} images for '{animal_name}'.")
        return

    # Use Google Custom Search API to search for images
    service = build('customsearch', 'v1', developerKey=API_KEY)

    # Modify query for "Amur Leopard"
    query = "Bonobo in the wild Africa"

    # Number of images downloaded
    image_count = 0

    # Perform multiple requests to fetch more than 10 images
    while image_count < additional_images_needed:
        # Calculate start index for pagination (within range 1-100)
        start_index = (image_count % 10) + 1
        # Calculate offset for results (number of previous full sets of 10)
        offset = (image_count // 10) * 10

        # Execute the search request
        res = service.cse().list(q=query, cx=CSE_ID, searchType='image', start=start_index + offset).execute()

        # Check if there are items in the response
        if 'items' in res:
            for item in res['items']:
                if image_count >= additional_images_needed:
                    break

                # Get image URL
                image_url = item['link']
                print(f"Downloading image: {image_url}")

                # Calculate the required number of digits for zero-padding
                num_digits = len(str(max_images))
                # Generate filename with zero-padding
                image_filename = f"{animal_name}_{str(existing_images + image_count + 1).zfill(num_digits)}.jpg"
                image_path = os.path.join(animal_dir, image_filename)

                try:
                    # Download image
                    response = requests.get(image_url)
                    response.raise_for_status()  # Raise an error for bad status codes

                    with open(image_path, 'wb') as f:
                        f.write(response.content)

                    image_count += 1
                except requests.exceptions.RequestException as e:
                    print(f"Failed to download {image_url}: {e}")

        # Break the loop if no more results are available
        if 'queries' in res and 'nextPage' not in res['queries']:
            break

    print(f"Downloaded {image_count} additional images for '{animal_name}'.")

# Usage example
folder_path = (r"C:\Users\getan\GitHub\ML\Endangered_Images")

animal = 'Bonobo'

get_animal_images_google(animal, save_root_dir, max_images=200)
