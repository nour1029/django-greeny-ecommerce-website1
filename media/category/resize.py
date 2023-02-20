from PIL import Image


for i in range(10):
    image = Image.open(f"({i+1}).jpg")
    resized_img = image.resize((250, 120))
    resized_img.save(f"({i+1}).jpg")
