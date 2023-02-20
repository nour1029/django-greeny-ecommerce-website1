from PIL import Image

def resize_all_folder(count):
    for i in range(count):
        image = Image.open(f"({i+1}).jpg")
        resized_img = image.resize((250, 120))
        resized_img.save(f"({i+1}).jpg")



image = Image.open(f"matebook-d-16-list.png")
resized_img = image.resize((250, 120))
resized_img.save(f"matebook-d-16-list-resized.jpg")
