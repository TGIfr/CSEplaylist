from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin


def get_nested_links_from_list(links, level=1):
    res = []
    for l in links:
        res.extend(get_nested_links(l, level))

    return res


def get_nested_links(link, level=1):
    if level < 1:
        return []

    # first iteration
    res_links = get_links(link)
    if link not in res_links:
        res_links.append(link)

    current_level_links = []
    for x in range(1, level):

        for l in res_links:
            current_level_links.extend(get_links(l))

        # check for duplicates
        for l in current_level_links:
            if l not in res_links:
                res_links.append(l)

    return res_links
    # print(link.get("href"))


def get_links(link):
    try:
        html_page = urlopen(link)
    except Exception:
        print(link + " - connection problems")
        return []

    soup = BeautifulSoup(html_page, "html.parser")

    links = []
    for l in soup.findAll("a"):
        curl = l.get("href")
        if curl is not None and "#" not in curl:
            full_link = curl
            if "http://" not in curl or "https://" not in curl:
                full_link = urljoin(link, curl)
            if full_link not in links:
                links.append(full_link)

    return links
