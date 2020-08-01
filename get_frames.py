import cv2
from conf import conf

frameFrequency = 1

video = cv2.VideoCapture(conf["video_file"])
if not video.isOpened():
    exit(0)

fps = video.get(cv2.CAP_PROP_FPS)

total_frame = 0
frame_id = 0
while True:
    ret, frame = video.read()
    if ret is False:
        break
    total_frame += 1
    if total_frame % frameFrequency == 0:
        frame_id += 1
        image_name = "{}\\frame_{}.jpg".format(conf["img_folder"], str(frame_id).zfill(10))
        cv2.imwrite(image_name, frame)
        print(image_name)
