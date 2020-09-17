import os
import csv
import numpy as np
import pandas as pd


# Req. 3-1	이미지 경로 및 캡션 불러오기 return img_paths, captions
def get_path_caption():
    csv_file = pd.read_csv('./datasets/captions.csv',
                           sep='|', header=[0], encoding='CP949')
    img_path_list = csv_file['image_name'].values.tolist()
    caption_list = csv_file[' comment'].values.tolist()
    return img_path_list, caption_list


# Req. 3-2	전체 데이터셋을 분리해 저장하기 return train_dataset_path, val_dataset_path
def dataset_split_save(ratio, seed):
    original_data = pd.read_csv(
        './datasets/captions.csv', sep='|', header=[0], encoding='CP949')
    train_dataset_path = original_data.sample(frac=ratio, random_state=seed)
    val_dataset_path = original_data.drop(train_dataset_path.index)
    train_dataset_path.to_csv('./datasets/captions_train.csv',
                              sep='|', header=['image_name', 'comment_number', 'comment'])
    val_dataset_path.to_csv('./datasets/captions_test.csv',
                            sep='|', header=['image_name', 'comment_number', 'comment'])
    return train_dataset_path.values.tolist(), val_dataset_path.values.tolist()


# Req. 3-3	저장된 데이터셋 불러오기 return img_paths, caption
def get_data_file(st):
    if st == 'train':
        csv_file = pd.read_csv(
            './datasets/captions_train.csv', sep='|', header=[0], engine='python')
        img_path_list = csv_file['image_name'].values.tolist()
        caption_list = csv_file['comment'].values.tolist()
        return img_path_list, caption_list
    elif st == 'test':
        csv_file = pd.read_csv(
            './datasets/captions_test.csv', sep='|', header=[0], engine='python')
        img_path_list = csv_file['image_name'].values.tolist()
        caption_list = csv_file['comment'].values.tolist()
        return img_path_list, caption_list
    else:
        raise ValueError


# Req. 3-4	데이터 샘플링
def sampling_data(image_name, caption, ratio):
    sample_image_name = pd.DataFrame(image_name).sample(frac=ratio)
    sample_caption = pd.DataFrame(caption).sample(frac=ratio)
    print(f'sampling data {ratio*100}%')
    return sample_image_name, sample_caption
