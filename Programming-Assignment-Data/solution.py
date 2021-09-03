import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

def main():
    # uses element tree to parse the xml file and saves root to root
    tree = ET.parse('com.pandora.android.xml')
    root = tree.getroot()

    # prints each child (only one) and its attributes
    # for child in root:
    #     print(child.tag, child.attrib)

    print()

    # prints all elements in the tree
    # print([elem.tag for elem in root.iter()])

    allbounds = []

    for node in root.iter():
        attributes = node.attrib
        bounds = attributes.get('bounds')
        if (bounds is not None) and (bounds != "[0,0][1440,2368]"):
            allbounds.append(bounds)

    print(allbounds)

    # convert string bounds into list of 4 integer coordinates
    for bound in allbounds:
        bound = bound.split(',')
        bound[0] = int(bound[0][1:])
        bound[2] = int(bound[2][:-1])
        tmp = bound[1].split(']')
        bound[1] = int(tmp[0])
        bound.insert(2, tmp[1])
        bound[2] = int(bound[2][1:])
        print(bound)
    return allbounds

    # String representation
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))

def pillow(bounds):
    img = Image.open('com.pandora.android.png')

    draw = ImageDraw.Draw(img)
    # draw.line((0, 0) + img.size, fill=128)
    # draw.line((0, img.size[1], img.size[0], 0), fill=128)
    # draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)
    draw.rectangle(
        (80, 2119, 336, 2368),
        outline=(0, 0, 0),
        width=10)

    img.show()

if __name__ == "__main__":
    allbounds = main()
    # pillow(allbounds)