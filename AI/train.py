from data import preprocess
from utils import utils
import pandas as pd

# config 저장
utils.save_config({'do_sampling': [True], 'conf2': [
                  'value2']}, 'new_conf.csv')
config = pd.read_csv("./new_conf.csv", sep='|').to_dict()

# 이미지 경로 및 캡션 불러오기
img_paths, captions = preprocess.get_path_caption()


# 전체 데이터셋을 분리해 저장하기
train_dataset_path, val_dataset_path = preprocess.dataset_split_save(0.8, 2020)


# 저장된 데이터셋 불러오기
img_paths, captions = preprocess.get_data_file('train')


# 데이터 샘플링
if config['do_sampling'][0]:
    img_paths, caption = preprocess.sampling_data(img_paths, captions, 0.2)

# 이미지와 캡션 시각화 하기
utils.visualize_img_caption(img_paths[0][0], captions[0])
