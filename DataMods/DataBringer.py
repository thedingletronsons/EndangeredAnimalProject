from googleapiclient.discovery import build
import os
import requests

# Google API key and Custom Search Engine ID
API_KEY = 'AIzaSyCUPMLQQN4P0RmuxKeUR5yq_13umlipks0'
CSE_ID = '3048a6d7aa0fe4939'


def get_animal_images_google(animal_name, save_root_dir, max_images=50):
    # Create directory path for the current animal
    animal_dir = os.path.join(save_root_dir, animal_name.replace(' ', '_'))

    # Ensure directory exists or create it
    if not os.path.exists(animal_dir):
        os.makedirs(animal_dir)

    # Use Google Custom Search API to search for images
    service = build('customsearch', 'v1', developerKey=API_KEY)
    query = f"{animal_name} endangered species"  # Modify query as needed

    # Number of images downloaded
    image_count = 0

    # Perform multiple requests to fetch more than 10 images
    while image_count < max_images:
        # Calculate start index for pagination
        start_index = image_count + 1

        # Execute the search request
        res = service.cse().list(q=query, cx=CSE_ID, searchType='image', start=start_index).execute()

        # Check if there are items in the response
        if 'items' in res:
            for item in res['items']:
                if image_count >= max_images:
                    break

                # Get image URL
                image_url = item['link']

                # Generate filename
                image_filename = f"{animal_name}_{image_count + 1}.jpg"
                image_path = os.path.join(animal_dir, image_filename)

                # Download image
                response = requests.get(image_url)
                with open(image_path, 'wb') as f:
                    f.write(response.content)

                image_count += 1

        # Break the loop if no more results are available
        if 'queries' in res and 'nextPage' not in res['queries']:
            break

    print(f"Downloaded {image_count} images for '{animal_name}'.")


# Usage example
save_root_dir = r'/Endangered_Images'
animals = [
#'African_forest_elephant',
#'Amur_Leopard',
#'Black_Rhino',
#'Bornean_Orangutan',
#'Cross_River_Gorilla',
    'Eastern_Lowland_Gorilla',
    'Hawksbill_Turtle',
    'Javan_Rhino',
    'Orangutan',
    'Saola',
    'Sumatran_Elephant',
    'Sumatran_Orangutan',
    'Sumatran_Rhino',
    'Sunda_Tiger',
    'Vaquita',
    'Western_Lowland_Gorilla',
    'Yangtze_Finless_Porpoise',
    'African_savanna_elephant',
    'African_Wild_Dog',
    'Asian_Elephant',
    'Black-footed_Ferret',
    'Blue_Whale',
    'Bluefin_Tuna',
    'Bonobo',
    'Bornean_Elephant',
    'Chimpanzee',
    'Fin_Whale',
    'Galapagos_Penguin',
    'Ganges_River_Dolphin',
    'Green_Turtle',
    'Hectors_Dolphin',
    'Humphead_Wrasse',
    'Indian_Elephant',
    'Indus_River_Dolphin',
    'Irrawaddy_Dolphin',
    'Monarch_Butterfly',
    'Mountain_Gorilla',
    'North_Atlantic_Right_Whale',
    'Red_Panda',
    'Sea_Lions',
    'Sea_Turtle',
    'Sei_Whale',
    'Sri_Lankan_Elephant',
    'Tiger',
    'Whale',
    'Whale_Shark',
    'Bigeye_Tuna',
    'Black_Spider_Monkey',
    'Dugong',
    'Giant_Panda'
]

for animal in animals:
    get_animal_images_google(animal, save_root_dir, max_images=100)
