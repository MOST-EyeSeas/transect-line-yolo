import os 
import shutil
import random
from pathlib import Path
from math import floor


class Dataset():
    def __init__(self, val_ratio, test_ratio) -> None:
        self.val_ratio = val_ratio
        self.test_ratio = test_ratio
        
        data_raw_path = os.path.join(os.getcwd(), 'data_raw')
        self.images_raw_path = os.path.join(data_raw_path, 'images')
        self.labels_raw_path = os.path.join(data_raw_path, 'bounding_box')

        self.data_set_path = os.path.join(os.getcwd(), 'data_set')
        self.images_set_path = os.path.join(self.data_set_path, 'images')
        self.labels_set_path = os.path.join(self.data_set_path, 'bounding_box')


    def save_data(self):
        shutil.rmtree(self.data_set_path)

        for split in ['train', 'val', 'test']:
                (Path(self.data_set_path) / split / 'images').mkdir(parents=True, exist_ok=True)
                (Path(self.data_set_path) / split / 'labels').mkdir(parents=True, exist_ok=True)
            
        # Get list of image files
        image_files = [f for f in os.listdir(self.images_raw_path ) if os.path.isfile(os.path.join(self.images_raw_path , f))]
        
        # Shuffle the image files
        random.shuffle(image_files)
        
        # Calculate the number of validation and test samples
        total_images = len(image_files)
        num_test = floor(total_images * self.test_ratio)
        num_val = floor(total_images * self.val_ratio)
        num_train = total_images - num_test - num_val
        
        # Split the data
        train_files = image_files[:num_train]
        val_files = image_files[num_train:num_train+num_val]
        test_files = image_files[num_train+num_val:]
        
        # Helper function to copy files
        def copy_files(file_list, split):
            for file_name in file_list:
                image_src = os.path.join(self.images_raw_path, file_name)
                label_src = os.path.join(self.labels_raw_path, Path(file_name).stem + '.txt')
                image_dst = os.path.join(self.data_set_path, split, 'images', file_name)
                label_dst = os.path.join(self.data_set_path, split, 'labels', Path(file_name).stem + '.txt')
                
                if os.path.exists(image_src) and os.path.exists(label_src):
                    shutil.copy2(image_src, image_dst)
                    shutil.copy2(label_src, label_dst)
        
        # Copy the files to the respective directories
        copy_files(train_files, 'train')
        copy_files(val_files, 'val')
        copy_files(test_files, 'test')
        
        print(f'Data split complete. Total: {total_images}, Train: {num_train}, Val: {num_val}, Test: {num_test}')
    