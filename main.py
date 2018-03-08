from functools import reduce

import xmlHelper
import nesting
from htmltags import hrefs, mp3refs

links = xmlHelper.parse('links.xml')

# for l in links:
#     print(l)

xmlHelper.save('dich.xml', links)
# print(links)
# links = nesting.get_nested_links_from_list(links, 2)
# for l in links:
#     print(l)
# print(hrefs(links[0], nested=2))
page_urls = reduce(lambda a, l: a or hrefs(l, nested=4), links, set())
print('Page urls')
print(page_urls)

mp3urls = reduce(lambda a, url: a + mp3refs(url), list(page_urls)[0], [])
print("mp3 urls")
print(mp3urls)

