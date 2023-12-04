import praw
import pyttsx3
import os
import time
from moviepy.editor import VideoFileClip, AudioFileClip
import random

# Replace these with your own values
CLIENT_ID = '6H6jyQzIQECton2W4dvLbQ'
CLIENT_SECRET = 'OTeI4XMbLUgFJZ2d7y94cxUi5Od9Iw'
USERNAME = 'Ploob-sr'
PASSWORD = 'ryerty1t'
USER_AGENT = 'MyAPI/0.0.1'

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT,
)

# Specify the subreddit
subreddit_name = 'confession'
subreddit = reddit.subreddit(subreddit_name)

post_index=5;
top_posts = subreddit.top(time_filter='week', limit=post_index + 1)

full_text=""

for index, submission in enumerate(top_posts):
    if index == post_index:
        full_text+=submission.title
        full_text+=submission.selftext
        break

#TTS
def text_to_speech_with_customization(text, output_file='output.mp3'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        if(i==0):
            engine.setProperty('voice', voice.id)
            break 

    rate=1.25 # no clue
    engine.setProperty('rate', int(175 * rate))

    engine.save_to_file(text, output_file)
    engine.runAndWait()

text_to_speech_with_customization(full_text)


time.sleep(1)

video_path = 'rawGameplay/Gameplay1.mp4'
video_clip = VideoFileClip(video_path)

audio_path = 'output.mp3'
audio_clip = AudioFileClip(audio_path)

start = random.random() * 0.9 * (video_clip.duration-audio_clip.duration)
video_clip = video_clip.subclip(start, start + audio_clip.duration)

video_clip = video_clip.set_audio(audio_clip)

output_path = 'finished/output_video.mp4'
video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

video_clip.close()
audio_clip.close()