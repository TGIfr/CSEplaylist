from functools import reduce
from tqdm import tqdm, trange

import xmlHelper
import id3
from htmltags import hrefs, mp3refs


def main():
    links = xmlHelper.parse("links.xml")

    xmlHelper.save("dich.xml", links)
    page_urls = reduce(lambda a, l: a or hrefs(l, nested=2), tqdm(links, leave=False), set())
    print("Page urls")
    print(page_urls)

    mp3urls = reduce(lambda a, url: a + mp3refs(url), tqdm(page_urls, leave=False), [])
    print("mp3 urls")
    print(mp3urls)
    print(list(filter(lambda url: "Alternative" in id3.get_genre(url), tqdm(mp3urls, leave=False))))


main()
