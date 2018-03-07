import re
from functools import reduce
from typing import List

from bs4 import BeautifulSoup
from urllib import request


def hrefs(url: str, nested: int = 1) -> set:
    if nested <= 0:
        return set()
    if nested == 1:
        soup = BeautifulSoup(request.urlopen(url))
        return set(a["href"] for a in soup.find_all("a"))

    return reduce(lambda a, x: a or hrefs(url, nested - 1), hrefs(url), set())


def genre(url: str) -> str:
    return 'rock' + url


def mp3refs(url: str) -> List[str]:
    # return re.findall("https?.+\.mp3", str(request.urlopen(url).read()))
    return re.findall("https?(\w|[./0-9])+?\.mp3", str(request.urlopen(url).read()))