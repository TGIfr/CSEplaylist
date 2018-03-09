import re
from functools import reduce
from typing import List
from bs4 import BeautifulSoup, UnicodeDammit
from urllib import request, parse


def hrefs(url: str, nested: int = 1) -> set:
    if nested <= 0:
        return set()

    if nested == 1:
        res = request.urlopen(url)
        if "text/html" in res.headers["content-type"]:
            soup = BeautifulSoup(res, "html.parser")
            return set(parse.urljoin(url, a.get("href")) for a in soup.find_all("a"))
        else:
            return set()

    return reduce(lambda a, x: a or hrefs(url, nested - 1), hrefs(url), set())


def mp3refs(url: str) -> List[str]:
    unicode = UnicodeDammit(request.urlopen(url).read()).unicode_markup
    return [parse.urljoin(url, el) for el in re.findall(r"https?://.+\.mp3\b", unicode)]
