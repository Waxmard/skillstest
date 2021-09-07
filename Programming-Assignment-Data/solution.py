import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

xmlFiles = ['com.apalon.ringtones.xml',
            'com.dropbox.android.xml',
            'com.giphy.messenger-1.xml',
            'com.giphy.messenger-2.xml',
            'com.google.android.apps.transalte.xml',
            'com.pandora.android.xml',
            'com.yelp.android.xml']

def main():
    for file in xmlFiles:
        bounds = xmlParse(file)
        painter(bounds, file)

# returns significant pixel bounds into a list of lists, each list has 4 coordinates of the corners of the rectangle that need to be drawn 
def xmlParse(currentFile):

    # uses element tree to parse the xml file and saves root to root
    tree = ET.parse(currentFile)
    root = tree.getroot()

    # saves all string bounds from each node to allbounds
    allbounds = []
    for node in root.iter():
        attributes = node.attrib
        bounds = attributes.get('bounds')
        # [0,0][1440,2368] is always the edge of the screen, this highlight is trivial and not needed
        if (bounds is not None) and (bounds != "[0,0][1440,2368]"):
            allbounds.append(bounds)

    return convertInt(allbounds)

# converts the string bounds from allbounds into lists (of 4 integer coordinates)
def convertInt(stringBounds):
    intbounds = []
    for bound in stringBounds:
        bound = bound.split(',')
        bound[0] = int(bound[0][1:])
        bound[2] = int(bound[2][:-1])
        tmp = bound[1].split(']')
        bound[1] = int(tmp[0])
        bound.insert(2, tmp[1])
        bound[2] = int(bound[2][1:])
        intbounds.append(bound)
    return intbounds

# draws the rectangles on the image then outputs it in Preview
def painter(bounds, currentFile):
    # imageFile is the xml files' string name with .png extension instead of .xml
    imageFile = currentFile.replace('xml', 'png')

    img = Image.open(imageFile)
    draw = ImageDraw.Draw(img)
    
    # draws rectangle over all significant bounds specified within xml file
    for bound in bounds:
        draw.rectangle(
        (bound[0], bound[1], bound[2], bound[3]),
        outline=('yellow'),
        width=5
        )

    img.show()

if __name__ == "__main__":
    main()