import csv
import cv2
from optparse import OptionParser
import os
from conf import conf


def get_img_file_nbr(file_name):
    return int(file_name.split(".")[0].strip("frame_"))


def get_img_file_name(img_nbr):
    return "frame_{}.jpg".format(str(img_nbr).zfill(10))


parser = OptionParser()
parser.add_option('--trail', default=str(999999999))
(options, args) = parser.parse_args()
trail = int(options.trail)

color = (212, 0, 255)
thickness = 4

coords = []
with open(conf["gap_fill_coord_file"]) as f:
    for img in csv.DictReader(f):
        coords.append(img)

for c in coords:
    c["x"] = int(c["x"])
    c["y"] = int(c["y"])

# add follow flight to the images with shot tracking
for cur_img in coords[1:]:
    img_path = "{}\\{}".format(conf["img_folder"], cur_img["img_name"])
    print(img_path)
    img = cv2.imread(img_path)
    for hist_c in [img for img in coords if img["img_name"] <= cur_img["img_name"]]:
        first_coord = (hist_c["img_name"] == coords[0]["img_name"])
        outside_trail = get_img_file_nbr(
            cur_img["img_name"]) - get_img_file_nbr(hist_c["img_name"]) >= trail
        if not first_coord and not outside_trail:
            cv2.line(img, pt1=(x, y), pt2=(
                hist_c["x"], hist_c["y"]), color=color, thickness=thickness)
        x, y = hist_c["x"], hist_c["y"]
    output_file = "{}\\{}".format(
        conf["processed_img_folder"], cur_img["img_name"])
    cv2.imwrite(output_file, img)

# add follow flight to all frames after the shot is done being tracked
last_coord = coords[-1]["img_name"]
img_names = os.listdir(conf["img_folder"])

for img_name in [i for i in img_names if i > last_coord]:
    img_path = "{}\\{}".format(conf["img_folder"], img_name)
    print(img_path)
    img = cv2.imread(img_path)
    for hist_c in coords:
        first_coord = (hist_c["img_name"] == coords[0]["img_name"])
        outside_trail = get_img_file_nbr(
            img_name) - get_img_file_nbr(hist_c["img_name"]) >= trail
        if not first_coord and not outside_trail:
            cv2.line(img, pt1=(x, y), pt2=(
                hist_c["x"], hist_c["y"]), color=color, thickness=thickness)
        x, y = hist_c["x"], hist_c["y"]
    output_file = "{}\\{}".format(conf["processed_img_folder"], img_name)
    cv2.imwrite(output_file, img)
