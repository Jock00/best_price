import requests
from lxml.html import fromstring
from urllib.parse import urljoin



### returns a list of [name, url] for phones
def altex_discovery(headers):


    start_url = "https://altex.ro/telefoane/cpl/"

    r = requests.get(start_url, headers=headers)
    data = fromstring(r.text)

    all_phones = []
    base_url = "https://altex.ro/telefoane/cpl/filtru/p/{}/"
    current_page = 1
    while True:
        phones = data.xpath("//*[contains(@class, 'Product ')]")
        if phones:
            for phone in phones:
                phone_name = phone.xpath(".//text()")[1]
                phone_url = phone.xpath(".//@href")[1]
                phone_url = urljoin(base_url, phone_url)
                all_phones.append((phone_name, phone_url))
            current_page += 1
            current_url = base_url.format(current_page)

            r = requests.get(current_url, headers=headers)
            data = fromstring(r.text)
        else:
            break
    return all_phones



