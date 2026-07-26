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