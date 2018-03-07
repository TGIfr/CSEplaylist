import xml.etree.ElementTree as ET


def parse(filename):
    links = ET.parse(filename).getroot().findall('link')
    return [l.text for l in links]


def save(filename, songs):
    root = ET.Element('songs')
    for song in songs:
        item = ET.SubElement(root, 'song')
        item.text = song

    data = ET.tostring(root, encoding = "unicode")
    file = open(filename, "w")
    file.write(data)
    return data
