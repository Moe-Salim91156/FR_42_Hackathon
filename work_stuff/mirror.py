import os
from PIL import Image


def mirror_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            try:
                img = Image.open(filepath)
                rgb_img = img.convert('RGB')
                mirrored_img = rgb_img.transpose(Image.FLIP_LEFT_RIGHT)
                name, ext = os.path.splitext(filename)
                output_path = os.path.join(output_dir, f"{name}_mirrored{ext}")
                mirrored_img.save(output_path)
                print(f"Mirrored: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
input_directory = './beiruit_images'
output_directory = './mirrored_images'
mirror_images(input_directory, output_directory)