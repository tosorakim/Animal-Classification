import os
import re
import cv2
import numpy as np
import csv
## 이미지 path 설정
def image_load(path):
    file_list=os.listdir(path)   
    file_name=[int(re.sub('[^0-9]','',i)) for i in file_list];file_name.sort() # 숫자가 아닌것은 '' 로 변경해라
    file_res= ['{}/{}.jpg'.format(path,j) for j in file_name]
        #file_res.append('%s\\%d.jpg' %(path,j))       
        
    image=[cv2.imread(k) for k in file_res]
        
    return np.array(image)


def label_load(path):
    file=open(path)
    label_data=csv.reader(file)
    label_list=np.array([i for i in label_data]).astype('int')    # astype 은 list 에 적용안됨
    label=np.eye(2)[label_list]     # 이진분류니까 2로 변경
    label=label.reshape(-1,2)     # 이진분류니까출력 노드는 2개니까 열을 2로 변경
    return label


def next_batch(data1, data2, init, fina):
    return data1[init : fina] , data2[init : fina]


def shuffle_batch(data_list, label):
    x=np.aragne(len(data_list))
    random.shuffle(x)
    data_list2 = data_list[x]
    label2=label[x]
    returndata_list2,label2