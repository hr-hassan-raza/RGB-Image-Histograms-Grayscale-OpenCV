import cv2
import matplotlib.pyplot as plt

def show_grayscale_equalized(img_path):
    image = cv2.imread(img_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eq_grayscale_image = cv2.equalizeHist(grayscale_image)
    fig = plt.figure(figsize=(7, 7))
    fig.add_subplot(1, 2,1)
    plt.imshow(eq_grayscale_image, cmap='gray')
    plt.title('Gray Scale Equalized histogram')
    fig.add_subplot(1, 2,2)
    plt.imshow(image, cmap='gray')
    plt.title('Original image')
    plt.show()

def show_rgb_equalized(img_path):
    image = cv2.imread(img_path)
    channels = cv2.split(image)
    eq_channels = []
    for ch, color in zip(channels, ['B', 'G', 'R']):
        eq_channels.append(cv2.equalizeHist(ch))

    eq_image = cv2.merge(eq_channels)
    eq_image = cv2.cvtColor(eq_image, cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize=(7, 7))
    fig.add_subplot(1, 2,1)
    plt.imshow(eq_image, cmap='gray')
    plt.title('RGB Equalized histogram')
    fig.add_subplot(1, 2,2)
    plt.imshow(image, cmap='gray')
    plt.title('Original image')
    plt.show()

show_grayscale_equalized('cat.jpg')
show_rgb_equalized('cat.jpg')