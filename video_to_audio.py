import moviepy.editor

# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("/home/ibm/Music/test.mp4")

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile("/home/ibm/Music/sample.mp3")