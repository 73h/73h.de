import re


def url_fix(value: str) -> str:
    value = value.lower()
    value = value.replace("ä", "ae")
    value = value.replace("ö", "ae")
    value = value.replace("ü", "ae")
    value = value.replace("ß", "ss")
    return re.sub(r"[^a-z0-9-]+", "-", value).lower()
