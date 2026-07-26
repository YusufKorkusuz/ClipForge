from app.downloader import get_video_info


def main():
    print("=" * 50)
    print("🚀 ClipForge")
    print("=" * 50)

    url = input("YouTube linkini gir: ")

    info = get_video_info(url)

    print("\nVideo Bilgileri")
    print("-" * 50)
    print(f"Başlık : {info['title']}")
    print(f"Kanal  : {info['channel']}")
    print(f"Süre   : {info['duration']} saniye")
    print(f"İzlenme: {info['view_count']}")


if __name__ == "__main__":
    main()