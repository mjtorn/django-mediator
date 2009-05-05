# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from lxml import etree

def create_return(content, numberto=None, numberfrom=None, operator=None, price=None, delivery_req_url=None):
    root = etree.Element('sms')

    if numberto:
        root.set('numberto', numberto)

    if numberfrom:
        root.set('numberfrom', numberfrom)

    if operator:
        root.set('operator', operator)

    if price:
        root.set('price', price)

    if delivery_req_url:
        root.set('delivery_req_url', delivery_req_url)

    message_node = etree.SubElement(root, 'message')
    message_node.text = etree.CDATA(content)

    return root

# EOF

