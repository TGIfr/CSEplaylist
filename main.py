import xmlHelper
import nesting

links = xmlHelper.parse('links.xml')

for l in links:
    print(l)

xmlHelper.save('dich.xml', links)

links = nesting.get_nested_links_from_list(links, 2)

for l in links:
    print(l)
