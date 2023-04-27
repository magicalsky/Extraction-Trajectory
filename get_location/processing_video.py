import cv2
import os


# Define the save image function
# image:the name of the picture to be saved
# addr; the image address with the first part of the photo name
# num: photo, suffix of name. int type
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)


# Generate a save directory
def mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


if __name__ == '__main__':
    # The location of the source video
    video_file_path = r'../Data/video/'
    # Source Video List
    video_list = os.listdir(video_file_path)
    # video_list.sort(key=lambda x: int(x[5:-4]))

    num = 1
    for video_name in video_list:
        print('processing {}'.format(video_name))
        # video_num = 'video'+str(num)
        save_path = '../result/frame/{}'.format(video_name)
        mkdir(save_path)    # Create save directory
        video_path = video_file_path+video_name
        # Read video files
        videoCapture = cv2.VideoCapture(video_path)
        # Read frames
        success, frame = videoCapture.read()
        i = 0
        # Set fixed frame rate
        timeF = 1
        j = 0
        while success:
            i = i + 1
            if (i % timeF == 0):
                j = j + 1
                save_image(frame, save_path+'/image', j)
                print('save image:', i)
            success, frame = videoCapture.read()
        num = num+1

