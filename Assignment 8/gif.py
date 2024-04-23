import os
import imageio

file_list=sorted(os.listdir("gif_pictures"),key=len)

IMAGES =[]
for file_name in file_list:
    image=imageio.imread("gif_pictures/"+file_name)
    IMAGES.append(image)

imageio.mimsave("assignment.gif",IMAGES)