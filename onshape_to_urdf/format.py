import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import decimal
import re

# Load the URDF XML file
urdf_file = '../urdf/sphere.urdf.xacro'
tree = ET.parse(urdf_file)
root = tree.getroot()


def round_string(string):
    values = string.split(" ")
    values = [float(v) for v in values]
    values = [round(v, 5) for v in values]
    return values
    
# Function to recursively update text in the XML tree
def update_text(node):
    for att in ["rgba", "xyz", "rpy"]:
        try:
            node.attrib[att] = round_string(node.attrib[att])
        except:
            pass

    for child in node:
        update_text(child)

# Update numbers in the XML tree
update_text(root)

# Format the XML with tabs using minidom
xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(newl='')

# Write the formatted XML back to a file
with open(urdf_file, 'w') as f:
    f.write(xml_string)

print(f"Formatted URDF saved to {urdf_file}")
