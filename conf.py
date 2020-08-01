import os

conf = {
    "video_file": "video.mp4",
    "follow_flight_video_file": "video_follow_flight.avi",
    "audio_file": "audio.wav",
    "coord_file": "coordinates.csv",
    "gap_fill_coord_file": "coordinates_complete.csv",
    "img_folder": "{}\\frames".format(os.getcwd()),
    "processed_img_folder": "{}\\frames_processed".format(os.getcwd())
}
