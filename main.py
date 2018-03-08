# import xmlHelper
# import nesting
#
# links = xmlHelper.parse('links.xml')
#
# for l in links:
#     print(l)
#
# xmlHelper.save('dich.xml', links)
#
# res = nesting.get_nested_links_from_list(links, 1)
#
# for l in res:
#     print(l)


# def hrefs(url: str, nested: int = 1) -> set:
#     if nested <= 0:
#         return set()
#     if nested == 1:
#         soup = BeautifulSoup(urlopen(url))
#         return set(a["href"] for a in soup.find_all("a"))
#
#     return reduce(lambda a, x: a or hrefs(url, nested - 1), hrefs(url), set())
#
#
# list = hrefs(xmlHelper.parse('links.xml')[0])
#
# for i in list:
#     print(list)


import id3

url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3'
x = id3.get_genre(url)
print(x)