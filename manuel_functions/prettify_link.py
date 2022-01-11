from urllib.parse import parse_qs


def prettify_link(url: str) -> str:
    prettified_link = parse_qs(url)['url'][0]
    return prettified_link
