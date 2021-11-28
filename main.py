
import cv2
import numpy as np
import matplotlib.pyplot as plt

###RGB image to gray scale using average method
def RGB_Gray(img_path):
    img = cv2.imread(img_path)
    #we need to transform this in order that Matplotlib reads it correctly
    fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grayscale_average_img = np.mean(fix_img, axis=2)
    # (axis=0 would average across pixel rows and axis=1 would average across pixel columns.)
    #print(grayscale_average_img)
    fig = plt.figure(figsize=(7, 7))
    fig.add_subplot(1, 2,1)
    plt.imshow(grayscale_average_img, cmap='gray')
    plt.title('Gray scale average image')
    fig.add_subplot(1, 2,2)
    plt.imshow(img, cmap='gray')
    plt.title('Original image')
    plt.show()

def histogram_intensity(img_path):
    image = cv2.imread(img_path)
    
    ## histogram of RGB image
    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color = col)
        plt.xlim([0, 256])
    plt.title('Histogram of RGB image')
    plt.show()

    ## histogram of gray scale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    plt.plot(histogram, color='k')
    plt.title('Histogram of Gray Scale image')
    plt.show()

RGB_Gray('cat.jpg')
histogram_intensity('cat.jpg')