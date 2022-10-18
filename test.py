from keras.models import load_model

import cv2

import numpy as np

import sys

filepath = sys.argv[1]

REV_CLASS_MAP = {

    0: "rock",

    1: "paper",

    2: "scissors",

    3: "none"

}

def mapper(val):

    return REV_CLASS_MAP[val]

model = load_model("rock-paper-scissors-model.h5")
