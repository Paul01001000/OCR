import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

from os import listdir

# read image
root = "C:/Users/paul8/Documents/Uni/7. Thesis/Image Processing/OCR/"
folders = ["English","German","Korean"]
lang_list = [['en','de'],['de','en'],['ko','en']]
cur = 2
img_folder = root + folders[cur]

# instance text detector
reader = easyocr.Reader(lang_list[cur], gpu=False)
threshold = 0.5

for img_name in listdir(img_folder):
    img_path = img_folder + "/" + img_name
    print(img_path)
    img = cv2.imread(img_path)
    detected = reader.readtext(img)

    # draw bbox and text
    for _, t in enumerate(detected):
        print(t)
        with open(root + folders[cur] + "-out/" + img_name + ".txt", "a", encoding="utf-8") as f:
            f.write(str(t) + ";\n")

        try:
            bbox, text, score = t
        except ValueError:
            continue

        if score > threshold:
            pt1,pt2 = list(map(int,bbox[0])),list(map(int,bbox[2]))

            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 1)
            if cur != 2:
                cv2.putText(img, text, pt1, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    cv2.imwrite(root + folders[cur] + "-out/" + img_name + "-out.png", img)

    