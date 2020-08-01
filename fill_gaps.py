import csv
from conf import conf


def get_img_file_nbr(file_name):
    return int(file_name.split(".")[0].strip("frame_"))


def get_img_file_name(img_nbr):
    return "frame_{}.jpg".format(str(img_nbr).zfill(10))


coords = []
with open(conf["coord_file"]) as f:
    for img in csv.DictReader(f):
        coords.append(img)

for c in coords:
    c["x"] = int(c["x"])
    c["y"] = int(c["y"])

img_nbrs = [get_img_file_nbr(c["img_name"]) for c in coords]
print(img_nbrs)

for nbr in range(min(img_nbrs) + 1, max(img_nbrs)):
    file_name = get_img_file_name(nbr)
    if nbr not in img_nbrs:
        last_nbr = max([n for n in img_nbrs if n < nbr])
        next_nbr = min([n for n in img_nbrs if n > nbr])
        gap = next_nbr - last_nbr
        position = nbr - last_nbr
        last_coords = [c for c in coords if c["img_name"]
                       == get_img_file_name(last_nbr)][0]
        next_coords = [c for c in coords if c["img_name"]
                       == get_img_file_name(next_nbr)][0]
        x_delta = int((next_coords["x"] - last_coords["x"]) / gap * position)
        y_delta = int((next_coords["y"] - last_coords["y"]) / gap * position)
        coords.append({
            "img_name": file_name,
            "x": last_coords["x"] + x_delta,
            "y": last_coords["y"] + y_delta
        })

sorted_coords = sorted(coords, key=lambda k: k['img_name'])

with open(conf["gap_fill_coord_file"], "w") as f:
    header = "img_name,x,y"
    data = "\n".join(
        ["{},{},{}".format(c["img_name"], c["x"], c["y"])
         for c in sorted_coords]
    )
    f.write("{}\n{}".format(header, data))
