"""
Intercept a piece of the image (coordinate area)
Intercept coordinates
"""

import cv2
import os

# Cropping area
x1 = 263
x2 = 318
y1 = 60
y2 = 550


# Generate a save directory
def mkdir(path):
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)


if __name__ == '__main__':
    # List of files (video1, video2 ....)
    file_list = os.listdir(r'../result/frame')
    for file in file_list:
        print('processing：', file)
        # The location of the source image
        image_file_path = r'../result/frame/' + file
        # Source image list
        image_list = os.listdir(image_file_path)
        image_list.sort(key=lambda x: int(x[5:-4]))

        # The location where the intercepted image is saved
        save_path = r'../result/img_location/' + file
        mkdir(save_path)

        i = 1
        for image_name in image_list:
            image_path = os.path.join(image_file_path, image_name)
            im = cv2.imread(image_path)

            # 坐标
            im = im[x1:x2, y1:y2]

            # Prefix of the intercepted image name
            out_file_name = './image' + str(i)
            # File name of the saved image
            save_path_file = os.path.join(save_path, out_file_name + '.jpg')
            cv2.imwrite(save_path_file, im)
            i = i + 1
