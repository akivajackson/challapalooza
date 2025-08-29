import os
from PIL import Image

# Folder containing PNGs
input_folder = "/Users/work/My Drive (mohosomerville@gmail.com)/Challapalooza | MoHo Summer Jewish Music Festival/1. Brand & Marketing (Promotions)/tshirt/Challapalooza Sticker Images"
output_folder = "/Users/work/My Drive (mohosomerville@gmail.com)/Challapalooza | MoHo Summer Jewish Music Festival/1. Brand & Marketing (Promotions)/tshirt/Challapalooza Sticker Images/output"

# Make output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Max file size in bytes (800 KB)
MAX_SIZE = 800 * 1024

def compress_image(img, output_path):
    """Compress JPEG until under MAX_SIZE"""
    quality = 95
    img.save(output_path, "JPEG", quality=quality)
    while os.path.getsize(output_path) > MAX_SIZE and quality > 10:
        quality -= 5
        img.save(output_path, "JPEG", quality=quality)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        # Open PNG
        with Image.open(input_path) as im:
            # Convert RGBA to RGB if needed
            if im.mode in ("RGBA", "LA"):
                background = Image.new("RGB", im.size, (255, 255, 255))
                background.paste(im, mask=im.split()[3])  # 3 is alpha
                im = background
            else:
                im = im.convert("RGB")

            compress_image(im, output_path)
            print(f"Saved {output_path}")