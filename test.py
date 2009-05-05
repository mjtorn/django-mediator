#!/usr/bin/python
# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from mediator import utils

from lxml import etree

if __name__ == '__main__':
    doc = utils.create_return('Kala on punainen viisaus')
    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)

    doc = utils.create_return(u'Tänään sait kuudeksi kuukaudeksi vippiä prkl', price='900')
    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)

    doc = utils.create_return('Vastaus menee goatseen', delivery_req_url='http://goatse.cx/', price='900')
    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)

# EOF

