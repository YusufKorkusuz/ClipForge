import re


def sanitize_filename(filename: str) -> str:
    """
    Windows'ta yasak karakterleri temizler.
    """

    return re.sub(r'[<>:"/\\|?*]', "_", filename)