from lxml import objectify
from lxml import etree
from io import StringIO, BytesIO
path = 'C:/shaohuanzi/xml/Tobeconverted_RL72005_2024-3.xml'
#tree = etree.parse(path)
#etree.tostring(tree.getroot())\n",
parsed = objectify.parse(open(path,mode='rb'))
root = parsed.getroot()
data = []
skip_fields = ['comment']
for child in root.iter():
    el_data = {}
    if child.tag in skip_fields:
        continue
    path=child.getroottree().getpath(child)
    try:
        el_data[path] = child.pyval
    except:
        el_data[path] = 'empty'
    data.append(el_data)