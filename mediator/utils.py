# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from lxml import etree

def create_return(content):
    root = etree.Element('sms')

    message_node = etree.SubElement(root, 'message')
    message_node.text = etree.CDATA(content)

    return root

# EOF

