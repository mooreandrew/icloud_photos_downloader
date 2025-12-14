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

    suffix = ''
    if download_suffix:
        suffix = '-' + download_suffix

    _n, _e = os.path.splitext(filename)

    download_path = os.path.join(download_dir, _n + suffix + _e)
    return download_path
