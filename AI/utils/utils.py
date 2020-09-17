from datetime import datetime
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
import pandas as pd


# Req. 2-2	세팅 값 저장
def save_config(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, sep='|')


# Req. 4-1	이미지와 캡션 시각화
def visualize_img_caption(img_path, caption):
    img = mpimg.imread('./images/'+img_path)
    plt.title(caption)
    plt.imshow(img)
    plt.show()
