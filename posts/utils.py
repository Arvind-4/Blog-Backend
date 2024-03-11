import re
import uuid
import math
from typing import Tuple
from django.utils.html import strip_tags


def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r"\w+", word_string)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count / 38.0)
    return int(read_time_min)


def get_image_filename(file_name) -> Tuple[str, str]:
    extension = file_name.split(".")[-1]
    _file_name = file_name.split(".")[0]
    return _file_name, extension


def save_images(file_name, directory_name):
    _file_name, extension = get_image_filename(file_name)
    return "/".join([directory_name, f"{_file_name}-{uuid.uuid4().hex}.{extension}"])
