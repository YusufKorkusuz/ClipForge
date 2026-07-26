from app.logger import logger
from app.downloader import get_video_info, download_video


def main():
    logger.info("Program started")
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

    secim = input("\nVideoyu indir? (E/H): ").strip().lower()

    if secim == "e":
        print("\nİndiriliyor...\n")
        download_video(url)
        print("\n✅ İndirme tamamlandı!")

    else:
        print("\nİndirme iptal edildi.")


if __name__ == "__main__":
    main()
    logger.info("Program finished")