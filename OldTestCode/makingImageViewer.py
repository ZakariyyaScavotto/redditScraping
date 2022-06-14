import os
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
'''
Useful links:
https://pyimagesearch.com/2021/01/20/opencv-resize-image-cv2-resize/
https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
https://thispointer.com/python-how-to-use-global-variables-in-a-function/
'''
global frame, imageLabel, currentImageIndex, maxIndex, imageFiles

def forward():
    global frame, imageLabel, currentImageIndex, maxIndex, imageFiles
    currentImageIndex = currentImageIndex+1
    if currentImageIndex > maxIndex:
        currentImageIndex = 0
    currentFileName = 'images/'+imageFiles[currentImageIndex]
    currentImage = cv2.imread(currentFileName, 1)
    currentImage = imutils.resize(currentImage, height=700)
    currentImage = Image.fromarray(currentImage)
    tkImage = ImageTk.PhotoImage(image=currentImage)
    imageLabel.configure(image=tkImage)
    imageLabel.image = tkImage

def back():
    global frame, imageLabel, currentImageIndex, maxIndex, imageFiles
    currentImageIndex = currentImageIndex-1
    if currentImageIndex < 0:
        currentImageIndex = maxIndex
    currentFileName = 'images/'+imageFiles[currentImageIndex]
    currentImage = cv2.imread(currentFileName, 1)
    currentImage = imutils.resize(currentImage, height=700)
    currentImage = Image.fromarray(currentImage)
    tkImage = ImageTk.PhotoImage(image=currentImage)
    imageLabel.configure(image=tkImage)
    imageLabel.image = tkImage


frame = tk.Tk()
imageFiles = os.listdir('images')
currentImageIndex, maxIndex = 0, len(imageFiles)-1
currentFileName = 'images/'+imageFiles[currentImageIndex]
imageLabel = tk.Label(frame)
frame.title('Image Viewer')
frame.geometry('800x800')
currentImage = cv2.imread(currentFileName, 1)
currentImage = imutils.resize(currentImage, height=700)
currentImage = Image.fromarray(currentImage)
tkImage = ImageTk.PhotoImage(image=currentImage)
imageLabel.configure(image=tkImage)
imageLabel.pack()


backButton = tk.Button(frame, text="Back", command= lambda:back())
backButton.pack(side='left', padx=25)
forwardButton = tk.Button(frame, text="Forward", command= lambda:forward())
forwardButton.pack(side='right', padx=25)

frame.mainloop()

