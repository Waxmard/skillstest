import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

def main():
    # uses element tree to parse the xml file and saves root to root
    tree = ET.parse('com.pandora.android.xml')
    root = tree.getroot()

    # saves all string bounds from each node
    allbounds = []
    for node in root.iter():
        attributes = node.attrib
        bounds = attributes.get('bounds')
        if (bounds is not None) and (bounds != "[0,0][1440,2368]"):
            allbounds.append(bounds)

    # convert string bounds into list of 4 integer coordinates
    intbounds = []
    for bound in allbounds:
        bound = bound.split(',')
        bound[0] = int(bound[0][1:])
        bound[2] = int(bound[2][:-1])
        tmp = bound[1].split(']')
        bound[1] = int(tmp[0])
        bound.insert(2, tmp[1])
        bound[2] = int(bound[2][1:])
        intbounds.append(bound)

    return intbounds

def pillow(bounds):
    img = Image.open('com.pandora.android.png')

    draw = ImageDraw.Draw(img)
    
    for bound in bounds:
        draw.rectangle(
        (bound[0], bound[1], bound[2], bound[3]),
        outline=(0, 0, 0),
        width=10
        )

    img.show()

if __name__ == "__main__":
    bounds = main()
    pillow(bounds)