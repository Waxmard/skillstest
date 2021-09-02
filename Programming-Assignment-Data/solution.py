import xml.etree.ElementTree as ET

def main():
    # uses element tree to parse the xml file and saves root to root
    tree = ET.parse('com.pandora.android.xml')
    root = tree.getroot()

    # prints each child (only one) and its attributes
    for child in root:
        print(child.tag, child.attrib)

    print()

    # prints all elements in the tree
    print([elem.tag for elem in root.iter()])

    # String representation
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))

if __name__ == "__main__":
    main()