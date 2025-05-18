import os
from PIL import Image, ImageEnhance

def enhance_contrast(input_dir, output_dir, contrast_factor=1.5):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            try:
                img = Image.open(filepath)
                enhancer = ImageEnhance.Contrast(img)
                contrasted_img = enhancer.enhance(contrast_factor)
                name, ext = os.path.splitext(filename)
                output_path = os.path.join(output_dir, f"{name}{ext}")
                contrasted_img.save(output_path)
                print(f"Enhanced contrast for: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

input_directory = '../grayscale_images'
output_directory = '../contrasted_images'
enhance_contrast(input_directory, output_directory, contrast_factor=2)