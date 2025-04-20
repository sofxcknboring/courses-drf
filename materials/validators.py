from django.core.exceptions import ValidationError
from urllib.parse import urlparse


def youtube_url_validator(value):
    allowed_domain = "youtube.com"
    parsed_url = urlparse(value)

    if parsed_url.netloc and allowed_domain not in parsed_url.netloc:
        raise ValidationError("Разрешены только ссылки на youtube.com")
