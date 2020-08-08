import os

project_name = "elm_creek_6_recoil"
project_path = ".\\follow-flight-projects\\{}".format(project_name)

conf = {
    "video_file": "video.mp4",
    "slient_video_file": "follow_flight_silent.avi",
    "audio_file": "audio.wav",
    "coord_file": "coordinates.csv",
    "gap_fill_coord_file": "coordinates_complete.csv",
    "img_folder": ".\\frames",
    "processed_img_folder": ".\\frames_processed"
}

if not os.path.exists(project_path):
    os.makedirs(project_path)
os.chdir(project_path)

if not os.path.exists(conf["img_folder"]):
    os.makedirs(conf["img_folder"])

if not os.path.exists(conf["processed_img_folder"]):
    os.makedirs(conf["processed_img_folder"])
