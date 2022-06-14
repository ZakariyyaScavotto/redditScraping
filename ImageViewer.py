# Class for the image viewer
import os
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils

class ImageViewer(tk.Toplevel):
    global frame, imageLabel, currentImageIndex, maxIndex, imageFiles

    def forward(self):
        global frame, imageLabel, currentImageIndex, maxIndex, imageFiles
        self.currentImageIndex = self.currentImageIndex+1
        if self.currentImageIndex > self.maxIndex:
            self.currentImageIndex = 0
        self.currentFileName = 'images/'+self.imageFiles[self.currentImageIndex]
        self.currentImage = cv2.imread(self.currentFileName, 1)
        self.currentImage = imutils.resize(self.currentImage, height=700)
        self.currentImage = Image.fromarray(self.currentImage)
        self.tkImage = ImageTk.PhotoImage(image=self.currentImage)
        self.imageLabel.configure(image=self.tkImage)
        self.imageLabel.image = self.tkImage

    def back(self):
        global frame, imageLabel, currentImageIndex, maxIndex, imageFiles
        self.currentImageIndex = self.currentImageIndex-1
        if self.currentImageIndex < 0:
            self.currentImageIndex = self.maxIndex
        self.currentFileName = 'images/'+self.imageFiles[self.currentImageIndex]
        self.currentImage = cv2.imread(self.currentFileName, 1)
        self.currentImage = imutils.resize(self.currentImage, height=700)
        self.currentImage = Image.fromarray(self.currentImage)
        self.tkImage = ImageTk.PhotoImage(image=self.currentImage)
        self.imageLabel.configure(image=self.tkImage)
        self.imageLabel.image = self.tkImage

    def __init__(self):
        super().__init__()
        self.title('Image Viewer')
        screenWidth, screenHeight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(str(screenWidth)+'x'+str(screenHeight))
        self.imageFiles = os.listdir('images')
        self.currentImageIndex, self.maxIndex = 0, len(self.imageFiles)-1
        self.currentFileName = 'images/'+self.imageFiles[self.currentImageIndex]
        self.imageLabel = tk.Label(self)
        self.currentImage = cv2.imread(self.currentFileName, 1)
        self.currentImage = imutils.resize(self.currentImage, height=700)
        self.currentImage = Image.fromarray(self.currentImage)
        self.tkImage = ImageTk.PhotoImage(image=self.currentImage)
        self.imageLabel.configure(image=self.tkImage)
        self.imageLabel.pack()


        self.backButton = tk.Button(self, text="Back", command= lambda:self.back())
        self.backButton.pack(side='left', padx=25)
        self.forwardButton = tk.Button(self, text="Forward", command= lambda:self.forward())
        self.forwardButton.pack(side='right', padx=25)

# frame = ImageViewer()
# frame.mainloop()