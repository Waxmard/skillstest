import xml.etree.ElementTree as ET

def practice():
    tree = ET.parse('../practice/movies.xml')
    root = tree.getroot()

    # for child in root:
    #     print(child.tag, child.attrib)

    # print([elem.tag for elem in root.iter()])
    # print()
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))
    # for movie in root.iter('movie'):
    #     print(movie.attrib)

    print()
    for description in root.iter('description'):
        print(description.text)

    # print()
    # for movie in root.findall("./genre/decade/movie/[year='1992']"):
    #     print(movie.attrib)

    # print()
    # for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    #     print(movie.attrib)

def main():
    tree = ET.parse('com.apalon.ringtones.xml')
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)


if __name__ == "__main__":
    practice()