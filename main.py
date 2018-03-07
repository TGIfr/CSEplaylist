import xmlHelper

links = xmlHelper.parse('links.xml')

for l in links:
    print(l)

xmlHelper.save('dich.xml', links)
