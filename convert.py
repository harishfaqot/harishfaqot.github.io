from PIL import Image
import os

input_folder = "."      # folder asal
output_folder = "output"     # folder hasil kompres
max_size_kb = 100            # target size 100KB

os.makedirs(output_folder, exist_ok=True)

def compress_to_target_size(img_path, output_path, max_kb):
    img = Image.open(img_path).convert("RGB")
    
    quality = 95  
    step = 5

    # turunkan kualitas sampai ukuran <= target
    while quality > 5:
        img.save(output_path, "JPEG", quality=quality, optimize=True)
        size_kb = os.path.getsize(output_path) // 1024

        if size_kb <= max_kb:
            return True
        
        quality -= step

    return False

for file in os.listdir(input_folder):
    if file.lower().endswith(("png", "jpg", "jpeg", "webp", "bmp")):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".jpg")
        
        success = compress_to_target_size(input_path, output_path, max_size_kb)
        
        if success:
            print(f"✔ {file} → compressed")
        else:
            print(f"✖ {file} → cannot reach 100KB, saved with lowest quality")
