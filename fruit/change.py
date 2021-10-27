import glob
import numpy as np
import os 
import pandas as pd
import matplotlib.pyplot as plt
import shutil 
import random 
TRAIN_DIR="train"
# for folder in os.listdir(TRAIN_DIR):
#     os.makedirs(os.path.join("test1",folder))

for label in os.listdir(TRAIN_DIR):
    #print(label)
    images_files=glob.glob(os.path.join(TRAIN_DIR,label)+"/*")
    print(images_files)
    #print(images_files)
    for i in range(100):
        index=random.randint(0,len(images_files)-1)

        des_path=images_files[index]
        #print(des_path)
        if os.path.exists(des_path):
            print(1)
            source_path=des_path.replace("train","test1")
            shutil.move(des_path,source_path)
            
        else:
            continue
            