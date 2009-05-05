#!/usr/bin/python
# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from mediator import utils

from lxml import etree

if __name__ == '__main__':
    doc = utils.create_return('test')
    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)

# EOF

