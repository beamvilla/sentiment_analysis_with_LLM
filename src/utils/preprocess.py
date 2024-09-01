import regex as re


def remove_special_char(message: str) -> str:
    """
    Remove special case and emoji from message.
    """
    pattern = r"[^\u0E00-\u0E7Fa-zA-Z\d\s'?]|[ฯ฿]|[๐-๙]+|\xa0|ๆ"
    clean_text = re.sub(r",", " ", message)
    clean_text = re.sub(pattern, "", clean_text)
    clean_text = re.sub(r"[)]", " ", clean_text)
    return clean_text.strip()


def remove_url(message: str) -> str:
   """
   Remove html link from message.
   """
   pattern = r"http\S+|www.\S+"
   return re.sub(pattern, "", message)