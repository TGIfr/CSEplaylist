import re
from functools import reduce
from typing import List
from bs4 import BeautifulSoup, UnicodeDammit
from urllib import request, parse


def hrefs(url: str, nested: int = 1) -> set:
    if nested <= 0:
        return set()

    if nested == 1:
        soup = BeautifulSoup(request.urlopen(url), "html.parser")
        return set(parse.urljoin(url, a["href"]) for a in soup.find_all("a"))

    return reduce(lambda a, x: a or hrefs(url, nested - 1), hrefs(url), set())


def mp3refs(url: str) -> List[str]:
    unicode = UnicodeDammit(request.urlopen(url).read()).unicode_markup
    return [parse.urljoin(url, el) for el in re.findall(r"https?://.+\.mp3", unicode)]
