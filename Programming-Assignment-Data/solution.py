import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

def main():
    # uses element tree to parse the xml file and saves root to root
    tree = ET.parse('com.pandora.android.xml')
    root = tree.getroot()

    # prints each child (only one) and its attributes
    for child in root:
        print(child.tag, child.attrib)

    print()

    # prints all elements in the tree
    # print([elem.tag for elem in root.iter()])


    for node in root.iter():
        attributes = node.attrib
        if attributes.get('clickable') == 'true':
            print(attributes.get('bounds'))
        else:
            print(attributes.get('clickable'))
    # String representation
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))

def pillow():
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
    main()
    pillow()