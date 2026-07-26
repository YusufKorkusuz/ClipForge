from app.logger import logger
from app.utils import sanitize_filename
from yt_dlp import YoutubeDL


def get_video_info(url: str):
    options = {
        "quiet": True,
        "skip_download": True,
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "channel": info.get("channel"),
        "duration": info.get("duration"),
        "view_count": info.get("view_count"),
    }


def download_video(url: str):

    logger.info("Download started")

    options = {
        "outtmpl": lambda info: f"downloads/{sanitize_filename(info['title'])}.%(ext)s",
        "format": "best[ext=mp4]/best",
        "socket_timeout": 30,
        "retries": 10,
        "fragment_retries": 10,
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])

    logger.info("Download completed")