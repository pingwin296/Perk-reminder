import asyncio
import os
import subprocess

import cv2
import discord
from dotenv import load_dotenv


def check_for_template(image):
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    print(result.max())
    return (result >= threshold).any()


def get_stream_url(tiktok_url):
    result = subprocess.run(
        ["streamlink", "--stream-url", tiktok_url, "best"],
        capture_output=True,
        text=True
    )
    url = result.stdout.strip()
    return url


intents = discord.Intents.default()
bot = discord.Client(intents=intents)
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
stream_url = os.getenv("STREAM_URL")
template = cv2.imread("template.jpg")
channel_id = os.getenv("CHANNEL_ID")
user_id = os.getenv("USER_ID")
threshold = 0.7


@bot.event
async def on_ready():
    channel = None
    dm = None
    if user_id is not None:
        user = await bot.fetch_user(int(user_id))
        dm = await user.create_dm()
    if channel_id is not None:
        channel = bot.get_channel(int(channel_id))
    while True:
        stream = get_stream_url(stream_url)
        if "error" in stream:
            print("Can't find stream")
            await asyncio.sleep(20)
            continue
        video = cv2.VideoCapture(stream)
        if not video.isOpened():
            print("Can't download a video")
            await asyncio.sleep(20)
            continue
        ret, frame = video.read()
        if not ret or frame is None:
            print("Can't download a frame")
            await asyncio.sleep(20)
            continue
        cv2.imwrite("frame.png", frame)
        if not check_for_template(frame):
            await asyncio.sleep(20)
        else:
            if channel is not None:
                await channel.send("Little perk reminder")
            if dm is not None:
                await dm.send("Little perk reminder")
            await asyncio.sleep(120)


bot.run(token)
