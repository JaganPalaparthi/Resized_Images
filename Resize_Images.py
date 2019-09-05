import os
import cv2
pth="Give the Input Images Folder Name"
path1="Give the Output Images Folder Name"
a=os.listdir(pth)
print(a)
f=a
for i in f:
    X_data=[]
    X_img_file_paths=os.path.join(pth,i)
    X_img_file_paths1=str(X_img_file_paths)
    print(X_img_file_paths1)
    print(pth)
    filename = cv2.imread(X_img_file_paths1,cv2.IMREAD_COLOR)
  
    img = cv2.resize(filename,(300,300))
    X_data.append(img)
    print(img)
    cv2.imwrite(os.path.join(path1,i),img)
