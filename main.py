import cv2
import numpy as np


def construct_class_names(file_name="class_names"):
    with open(file_name, 'rt') as file:
        names = file.read().rstrip('\n').split('\n')
    return names


class_names = construct_class_names()
print(class_names)
