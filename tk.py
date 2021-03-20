import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import tkinter.simpledialog


root = tk.Tk()

#setting up a tkinter canvas
w = Canvas(root, width=900, height=900)
w.pack()

#adding the image
image = Image.open("parrot.jpg")
img_cv = cv2.imread('parrot.jpg')
im_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
original = image.resize((900,900)) #resize image
img = ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")

#main color selection function
def isolation(pixels):
    value = pixels
    rng = scale.get()
    curr_value = np.zeros(3)
    distance = 0
    dim = im_rgb.shape
    for i in range(dim[0]):
        for j in range(dim[1]):
            curr_value = np.squeeze(im_rgb[i, j, :])
            distance = np.sqrt(np.sum(np.power(curr_value - value, 2)))
            if distance > rng:
                im_rgb[i, j, :] = np.mean(np.squeeze(im_rgb[i, j, :]))
    plt.imshow(im_rgb)
    plt.show()



#surprise button
def blur():
    blur = cv2.medianBlur(im_rgb, 5)
    plt.imshow(blur)
    plt.show()



def on_click(eventorigin):
    global x,y
    x = eventorigin.x
    y = eventorigin.y
    pixel_values = image.getdata()
    tk.messagebox.showinfo("Selected pixel values", pixel_values[x*y])
    isolation(pixel_values[x*y])

scale = Scale(root, from_ = 0, to = 255, orient = HORIZONTAL, length = 100, label = "Color radius")
scale.place(x = 0, y = 0)

#mouseclick event
w.bind("<Button 1>",on_click)

btn2 = tk.Button(w, text="Surprise Button", command=blur, width=12)
btn2.place(x=800, y=3)

root.mainloop()
