"""
OCR extract coordinates
"""


import os
import cv2
from paddleocr import PaddleOCR


# Recognize coordinates
def get_location(image):
    # Read images
    img = cv2.imread(image)
    img_shape = img.shape
    h = img_shape[0]
    w = img_shape[1]
    # Color image conversion to grayscale image (3 channels to 1 channel)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    ret, gray = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
    dst = 255 - gray
    ocr = PaddleOCR(
        # lang='en',
        # use_angle_cls=True,
        # rec_model_dir=r'',
        # det_model_dir=r'',
        # cls_model_dir=r''
    )
    text = ocr.ocr(dst)
    print(text)
    if text:
        for t in text:
            result = t[1][0]
            print(result)
    else:
        result = 'do not get location'
        print(result)
    # return x, y, z
    return result


if __name__ == '__main__':
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    # List of files (video1, video2 ....)
    file_list = os.listdir(r'../result/img_location')
    for file in file_list:
        peo_id = file[0:2]
        print('Data for the {}th person is being processed'.format(peo_id))
        with open(r'../result/location_result/{}.txt'.format(file), 'a+', encoding='utf-8') as f:
            # The location of the image folder
            image_file_path = r'../result/img_location/' + file
            # Image List
            image_list = os.listdir(image_file_path)
            image_list.sort(key=lambda m: int(m[5:-4]))
            frame = 1
            for image_name in image_list:
                print('The {}th picture'.format(frame))
                image_path = image_file_path + '/' + image_name
                location = get_location(image_path)
                data_text = str(peo_id)+'/'+str(frame)+'/'+location+'\n'
                f.write(data_text)
                frame = frame + 1

