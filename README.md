# follow-flight
Rudimentary video and photo editing scripts for shot-tracking. Note that this project can only handle shot tracking for videos with a static camera position.

## Software Requirements
- [Python3](https://www.python.org/downloads/) with pip, the Python package manager
    * [opencv](https://pypi.org/project/opencv-python/) - for video and image editing in Python
        > `pip install opencv-python`
    * [moviepy](https://pypi.org/project/moviepy/) - for audio operations in Python
        >`pip install moviepy`
- [ffmpeg](https://ffmpeg.org/) - for CLI audio and video operations
    * After installing, add the ffmpeg `bin` folder to PATH

Since ffmpeg is a CLI tool, this project utilizes Powershell scripts, making some operations available to Windows users only. In order to use this functionality, Windows users must ensure that their PC security settings allow the execution of Powershell scripts.

## Creating Your First Shot Tracking Project

#### Project Setup

First, create a folder for your new project under the `follow-flight-projects` folder (no spaces or special characters). Set this as the `project_name` variable in `conf.py`.

Drop your video file into the new project folder in .mp4 format, and name it `video.mp4`.

Run `python get_frames.py`. This is a one-time operation that extracts all the frames from your video and saves them as .jpg image files to a project subfolder called `frames`. The name of each image indicates its frame position in the video.

Run `python get_audio.py`. This is a one-time operation that extracts the audio from the video and saves it as a `.wav` file, so it can be added back later to the final video.

#### Define the Shot Tracker Path

With the frames extracted, look through the image file to determine where your shot tracking should start (for example, frame 300). Then, run the `get_coords.py` script to manually set the coordinates of your shot. You'll want to pass the start frame of your shot as an argument to this script. Ex. `python get_coords.py --start 300`.

- To indicate the position of your disc in an image, simply click on the screen where you want the shot tracker to be. Click slightly behind the disc so the shot tracker line doesn't cover it in the final video.

- You may not want to set the position of the disc for each frame, depending on your video's FPS. This can result in an extremely "choppy" result. To skip a frame without indicating the position of the disc, hit the `ESC` key on your keyboard. We will run a script that fills in the gaps later.

- Once the flight of your disc is done, keep hitting the `ESC` key until you've gotten through all the frames of the video.

- The location of your shot tracker for each frame you selected will be stored in the `coordinates.csv` file.

#### Create the shot tracker video

To construct the final video, run the `make_video.ps1` script. This takes the following positional parameters:
1. <b>project name</b> (string) (required) - this is the name of your shot tracking folder
1. <b>trail</b> (integer) (optional) - this determines how many frames a piece of the shot tracking line will stay on the video before fading away
    - If not specified, the shot tracking line will persist until the end of the video
