import re


# this is stolen from Django Core docs
def validate_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    if re.match(regex, url) is None:
        return False
    return True


if __name__ == "__main__":
    print(validate_url("https://www.top10.com/hosting/comparison?monitoring=1&ts=rotw&ip=3.7.91.44"))
