from urllib.parse import parse_qs
from bs4 import BeautifulSoup
import requests


def parse_product_links(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,\
        application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/96.0.4664.93 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    src = resp.text

    # # Uncomment with the above to write page once
    # with open("../page.html", "w", encoding="utf-8") as file:
    #     file.write(src)

    # # Uncomment with the below to work with file and not URL (not to get bot-banned)
    # with open("page.html", encoding="utf-8") as file:
    #     src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_ctas = soup.select(".chart__body:not([data-cross-chart='true']) .right__CTA-container .cta-button")
    raw_product_links = [item.get("href") for item in all_ctas]
    product_links = []
    for link in raw_product_links:
        try:
            product_link = parse_qs(link)['url'][0]
            product_links.append(product_link)
        except KeyError:
            product_links.append("Non-paying")

    product_names = [item.get("data-product-name") for item in all_ctas]

    result = dict(zip(product_names, product_links))
    return result


if __name__ == "__main__":
    bad_URL = "https://www.top10.com/"
    good_URL = "https://www.top10.com/fitness-machines/comparison?monitoring=1"
    print(parse_product_links(good_URL))
