from moviepy.editor import *
from conf import conf

audioclip = AudioFileClip(conf["video_file"])
audioclip.write_audiofile(conf["audio_file"])
