from PIL import Image, ImageEnhance, ImageOps
import os
import random
import numpy as np

def augment_images_in_folder_random(folder_path, target_total=500):
    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    # Calculate the current number of images in the folder
    current_count = len(image_files)
    if current_count >= target_total:
        print(f"Already have {current_count} images. No augmentation needed.")
        return

    # Shuffle the list of image files to randomly select images
    random.shuffle(image_files)

    # Number of images to augment
    images_to_augment = target_total - current_count
    print(f"Current images: {current_count}, augmenting {images_to_augment} more images.")

    # Iterate over randomly selected image files and augment as needed
    for i in range(images_to_augment):
        filename = random.choice(image_files)
        image_path = os.path.join(folder_path, filename)
        original_image = Image.open(image_path)

        # Ensure the image is in RGB mode
        if original_image.mode != 'RGB':
            original_image = original_image.convert('RGB')

        # Apply augmentation techniques
        augmented_image = apply_augmentation(original_image)

        # Generate new filename with augmentation suffix
        augmented_filename = f"{os.path.splitext(filename)[0]}_augmented_{i+1}.jpg"
        augmented_image_path = os.path.join(folder_path, augmented_filename)

        try:
            # Save the augmented image
            augmented_image.save(augmented_image_path)
        except Exception as e:
            print(f"Failed to save {augmented_image_path}: {e}")

    print(f"Achieved {target_total} images in '{folder_path}'.")

def apply_augmentation(image):
    # Randomly rotate the image
    rotated_image = image.rotate(random.randint(-10, 10))

    # Randomly flip the image horizontally
    if random.random() > 0.5:
        flipped_image = ImageOps.mirror(rotated_image)
    else:
        flipped_image = rotated_image

    # Randomly flip the image vertically
    if random.random() > 0.5:
        flipped_image = ImageOps.flip(flipped_image)

    # Randomly adjust brightness
    enhancer = ImageEnhance.Brightness(flipped_image)
    brightened_image = enhancer.enhance(random.uniform(0.8, 1.2))

    # Randomly adjust contrast
    enhancer = ImageEnhance.Contrast(brightened_image)
    contrasted_image = enhancer.enhance(random.uniform(0.8, 1.2))

    # Add random noise
    noisy_image = add_noise(contrasted_image)

    return noisy_image

def add_noise(image):
    # Convert image to numpy array
    np_image = np.array(image)
    # Generate random noise
    noise = np.random.normal(0, 25, np_image.shape).astype(np.uint8)
    # Add noise to the image
    noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    # Convert back to PIL image
    return Image.fromarray(noisy_image)

# Usage example
folder_path = r"C:\Users\getan\GitHub\ML\Endangered_Images\Chinese_Giant_Salamander"

# Augment images in the specified folder to reach a total of 500 images
augment_images_in_folder_random(folder_path, target_total=500)
