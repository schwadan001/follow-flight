import csv
import cv2
import os
from conf import conf


def get_img_file_cv(file_name):
    print(file_name)
    processed_file_name = "{}\\{}".format(
        conf["processed_img_folder"], file_name
    )
    if os.path.isfile(processed_file_name):
        return cv2.imread(processed_file_name)
    else:
        return cv2.imread("{}\\{}".format(conf["img_folder"], file_name))


img_names = os.listdir(conf["img_folder"])

video = cv2.VideoCapture(conf["video_file"])
if not video.isOpened():
    exit(0)

fps = video.get(cv2.CAP_PROP_FPS)
codec = video.get(cv2.CAP_PROP_FOURCC)

first_img = get_img_file_cv(img_names[0])

height, width, layers = first_img.shape
video = cv2.VideoWriter(
    conf["follow_flight_video_file"], 0, fps, (width, height)
)

for img_name in img_names[1:]:
    video.write(get_img_file_cv(img_name))

cv2.destroyAllWindows()
video.release()
