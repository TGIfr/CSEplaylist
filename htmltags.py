import re
from functools import reduce
from typing import List

from musictools import musictools
from bs4 import BeautifulSoup, UnicodeDammit
from urllib import request
from urllib import parse
from stagger.id3 import *
import mutagen
import giofile
from gi.repository import Gio


def hrefs(url: str, nested: int = 1) -> set:
    if nested <= 0:
        return set()

    if nested == 1:
        soup = BeautifulSoup(request.urlopen(url), "html.parser")
        return set(parse.urljoin(url, a["href"]) for a in soup.find_all("a"))

    return reduce(lambda a, x: a or hrefs(url, nested - 1), hrefs(url), set())


def genre(url: str = '') -> str or None:
    metadata = musictools.get_metadata('http://upload.wikimedia.org/wikipedia/commons/transcoded'
                                       '/b/be/Anthem-of-Ukraine_Chorus_Veryovka.ogg/'
                                       'Anthem-of-Ukraine_Chorus_Veryovka.ogg.mp3')
    print('Metadata: ' + str(metadata))
    return metadata['GENRE']


def mp3refs(url: str) -> List[str]:
    soup = BeautifulSoup(request.urlopen(url), "html.parser")
    unicode = UnicodeDammit(request.urlopen(url).read()).unicode_markup
    soup.find_all("a", href=re.compile(r"\.mp3")) + soup.find_all("source", src=re.compile(r"\.mp3"))
    return [el for el in soup.find_all(lambda tag: re.compile(r"\.mp3").match(tag.href) or re.compile(r"\.mp3").match(tag.src))]
