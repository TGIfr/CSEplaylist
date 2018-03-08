import xmlHelper
import nesting

links = xmlHelper.parse('links.xml')

for l in links:
    print(l)

xmlHelper.save('dich.xml', links)

links = nesting.get_nested_links_from_list(links, 2)

for l in links:
    print(l)

from htmltags import hrefs, mp3refs

#print(hrefs("http://www.apple.com", nested=1))
# print(mp3refs("https://ru.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0"))
print(mp3refs("http://mp3party.net/music/8500219"))
# print(genre())