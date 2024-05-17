import cv2
import numpy as np


def construct_class_names(file_name="class_names"):
    with open(file_name, 'rt') as file:
        names = file.read().rstrip('\n').split('\n')
    return names


class_names = construct_class_names()
print(class_names)


capture = cv2.VideoCapture('objects.mp4')

while True:
    is_grabbed, frame = capture.read()
    if not is_grabbed:
        break

    cv2.imshow('Video', frame)
    cv2.waitKey(20)

capture.release()
cv2.destroyAllWindows()