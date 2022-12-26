import cv2 as cv
import numpy as np
import easygui
import imageio
import sys
import matplotlib.pyplot as plt
import sys
import os
import tkinter as tk

def upload():

    """ fileopenbox opens the box to choose file and choose file and help us store file path as string """
    
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):

    originalImage = cv.imread(ImagePath)

    # check if image was not chosen

    if originalImage is None:
        print("Cannot find any image. Choose appropriate file!")
        sys.exit()

    # read the image

    originalImage = cv.cvtColor(originalImage, cv.COLOR_BGR2RGB)
    resized1 = cv.resize(originalImage, (378, 496))

    # plt.imshow(resized1, cmap='gray')

    """ Multiple transfromaations have to be done on a image to make it into a cartoon like image. First transformation is into grayscale."""

    # converting an image into grayscale

    grayScaleImage = cv.cvtColor(originalImage, cv.COLOR_BGR2GRAY)
    resized2 = cv.resize(grayScaleImage, (378, 496))

    # plt.imshow(resized2, cmap='gray')

    """ Next transformation is to smooth the grayscale image """

    smoothGrayScale = cv.medianBlur(grayScaleImage, 5)
    resized3 = cv.resize(smoothGrayScale, (378, 496))

    # plt.imshow(resized3, cmap='gray')

    """ Next transformation is to retrieve the edges of the image """

    # retreiving the edges for cartoon effect by using the thresholding technique

    getEdge = cv.adaptiveThreshold(
        smoothGrayScale, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

    resized4 = cv.resize(getEdge, (378, 496))

    # plt.imshow(resized4, cmap='gray')

    """ Next transformation is to prepare a mask image """

    # applying bilateral filter to remove noise and keep edge sharp as required

    colorImage = cv.bilateralFilter(originalImage, 9, 9, 300, 300)
    resized5 = cv.resize(colorImage, (378, 496))

    # plt.imshow(resized5, cmap='gray')

    """ Next transformation is a give a cartoon effect """

    # masking edged image with our beautified image

    cartoonImage = cv.bitwise_and(colorImage, colorImage, mask = getEdge)
    resized6 = cv.resize(cartoonImage, (378, 496))

    # plt.imshow(resized6, cmap='gray')

    """ Plotting all the transformations """
    images = [resized1, resized2, resized3, resized4, resized5, resized6]

    fig, axes = plt.subplots(2, 3, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []}, gridspec_kw=dict(hspace=0.1, wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    # plt.show()

def save(resized6, ImagePath):

    """ saving the image using imwrite() """

    newName = "cartoonified_Image"
    path1 = os.path.dirname(upload.ImagePath)
    extension = os.path.splitext(upload.ImagePath)[1]
    save_path = os.path.join(path1, newName + extension)
    cv.imwrite(save_path, cv.cvtColor(resized6, cv.COLOR_RGB2BGR))

    save_msg = "Image saved as " + newName + " at " + save_path
    tk.messagebox.showinfo(title=None, message=save_msg)
