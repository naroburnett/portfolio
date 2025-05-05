from PIL import Image
from tqdm import tqdm
import os

def main():
    optimize_images_in_directory("Input", "Output")

def optimize_image(input_path, output_path):
    """
    Optimize an image by converting it to JPEG format and reducing its quality.
    
    :param input_path: Path to the input image file.
    :param output_path: Path to save the optimized image.
    """
    with Image.open(input_path) as img:
        img = img.convert("RGB")  # Convert to RGB if not already in that mode
        base, ext = os.path.splitext(output_path)
        new_output_path = f"{base}_optimized.jpg"  # Add '_optimized' to the filename
        img.save(new_output_path, "JPEG", quality=15)  # Save with reduced quality
        
def optimize_images_in_directory(input_dir, output_dir):
    """
    Optimize all images in a directory and save them to another directory.
    
    :param input_dir: Directory containing the input images.
    :param output_dir: Directory to save the optimized images.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in tqdm(os.listdir(input_dir), desc="Optimizing images"):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            optimize_image(input_path, output_path)
            print(f"Optimized {filename} and saved to {output_path}")

if __name__ == "__main__":
    main()
