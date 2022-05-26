from tqdm import tqdm
from time import sleep
from PIl import Image

import os

def Resize_image(size,image):
    if os.path.isfile(image):
        try:
            im = Image.open(image)
            im.thumbnail(size,Image.ANTIALIAS)
            im.save("resize/" + str(image) + ".jpg")
        except Exception as ex:
            print(f"Error: {str(ex)} to {image}")



path = input("Enter Path to images : ")
size = input("Size Height , Width : ")
size = tuple(map(int, size.split(",")))

os.chdir(path)

list_images = os.listdir(path)
if "resize" not in list_images:
    os.mkdir("resize")

for image in tqdm(list_images,desc="Resezing Images"):
    Rezing_image(size,image)
    sleep(0.1)
print("Resizing Completed!")

