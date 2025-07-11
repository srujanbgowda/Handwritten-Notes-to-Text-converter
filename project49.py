import os
from PIL import Image
import pytesseract

image_path = r"C:\Users\Admin\Desktop\notes.jpg"

if os.path.exists(image_path):
    print("✅ File found!")
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    print(text)
else:
    print("❌ File NOT found! Check your filename and path.")