import cv2
from optparse import OptionParser
import os
from conf import conf

parser = OptionParser()
parser.add_option('--start', default=str(0))
(options, args) = parser.parse_args()
start_img_name = "frame_{}.jpg".format(options.start.zfill(10))

window_name = "Frame"

with open(conf["coord_file"], "w") as f:
    f.write("img_name,x,y\n")

img_names = os.listdir(conf["img_folder"])

for img_name in [i for i in img_names if i >= start_img_name]:
    img_path = "{}\\{}".format(conf["img_folder"], img_name)
    img = cv2.imread(img_path)

    def get_coordinates(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            with open(conf["coord_file"], "a") as f:
                f.write("{},{},{}\n".format(img_name, x, y))
            cv2.destroyWindow(window_name)

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
    )
    cv2.setMouseCallback(window_name, get_coordinates)

    try:
        while cv2.getWindowProperty(window_name, 0) >= 0:
            cv2.imshow(window_name, img)
            if cv2.waitKey(10) & 0xFF == 27:
                break
    except cv2.error:
        pass
