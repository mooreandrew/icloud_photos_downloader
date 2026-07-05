"""Path functions"""

import os


def remove_unicode_chars(value: str) -> str:
    """Removes unicode chars from the string"""
    result = value.encode("utf-8").decode("ascii", "ignore")
    return result


def clean_filename(filename: str) -> str:
    """Replaces invalid chars in filenames with '_'"""
    invalid = '<>:"/\\|?*\0'
    result = filename

    for char in invalid:
        result = result.replace(char, "_")

    return result


def local_download_path(filename: str, download_dir: str, download_suffix: str) -> str:
    """Returns the full download path, including size"""

    filename2 = filename.split('.')[0] + download_suffix + filename.splt('.')[1]
    download_path = os.path.join(download_dir, filename2)
    return download_path
