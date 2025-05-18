import os
from PIL import Image

def create_grayscale_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            try:
                img = Image.open(filepath).convert('L')
                name, ext = os.path.splitext(filename)
                output_path = os.path.join(output_dir, f"{name}{ext}")
                img.save(output_path)
                print(f"Converted to grayscale: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")


input_directory = '../images'
output_directory = '../grayscale_images'
create_grayscale_images(input_directory, output_directory)
