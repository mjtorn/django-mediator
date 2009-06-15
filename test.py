#!/usr/bin/python
# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from mediator import utils

from lxml import etree

if __name__ == '__main__':
#### These are broken, let them be broken
#    doc = utils.create_return('Kala on punainen viisaus')
#    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)
#
#    doc = utils.create_return(u'Tänään sait kuudeksi kuukaudeksi vippiä prkl', price='900')
#    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)
#
#    doc = utils.create_return('Vastaus menee goatseen', delivery_req_url='http://goatse.cx/', price='900')
#    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)
#
#    try:
#        err = utils.create_error('This will fail', 'satan')
#    except TypeError, msg:
#        print 'successfully caught %s\n' % msg
#
#    doc = utils.create_error('Stupid user fault', 'user')
#    print etree.tostring(doc, xml_declaration=True, encoding='utf-8', pretty_print=True)

    smil_xml = """\
<?xml version="1.0" encoding="utf-8"?>
<mms numberto="666" numberfrom="+35850666" operator="Saunalahti" transactiond="700">
<subject><![CDATA[Te testiä]]></subject>
<presentation><![CDATA[
 <smil>
   <head>
    <layout>
      <root-layout width="176" height="208"/>
      <region id="Text" width="160" height="183" top="5" left="8" fit="scroll"/>
    </layout>
   </head>
   <body>
     <par dur="5000ms">
       <text region="Text" src="Te_testi.txt"/>
     </par>
   </body>
  </smil>
]]>
</presentation>
<media filename="Te_testi.txt" mimetype="text/plain">
   <text><![CDATA[Te testiä]]></text>
</media>
<media filename="" mimetype="image/jpeg">
  <data binlength="">
  </data>
</media>
</mms>
    """

    smil = etree.fromstring(smil_xml)

    medias = smil.findall('media')
    #media = [m for m in medias if m.attrib['mimetype'] == 'image/jpeg'] or None
    media = [m for m in medias if m.attrib['mimetype'].startswith('image/')] or None
    if media is None:
        print 'system error'
    elif len(media) > 1:
        print 'bad message'
    else:
        media = media[0]
        print 'ok %s' % media


# EOF

