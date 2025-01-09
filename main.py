import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

from os import listdir

# read image
img_folder = "C:/Users/paul8/Pictures/2023-12-20/"

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)
threshold = 0.5

for img_name in listdir(img_folder):
    img_path = img_folder + img_name
    img = cv2.imread(img_path)

    detected = reader.readtext(img)

    # draw bbox and text
    for _, t in enumerate(detected):
        print(t)

        bbox, text, score = t

        if score > threshold:
            cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
            cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

    