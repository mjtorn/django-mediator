# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from mediator import models

from lxml import etree

def create_return(content, sms, numberto=None, numberfrom=None, operator=None, price=None, delivery_req_url=None):
    root = etree.Element('sms')
    return_sms = models.ReturnSms()
    return_sms.sms = sms

    if numberto:
        root.set('numberto', numberto)
        return_sms.numberto = numberto

    if numberfrom:
        root.set('numberfrom', numberfrom)
        return_sms.numberfrom = numberfrom

    if operator:
        root.set('operator', operator)
        return_sms.operator = operator

    if price:
        root.set('price', price)
        return_sms.price = price

    if delivery_req_url:
        root.set('delivery_req_url', delivery_req_url)
        return_sms.delivery_req_url = delivery_req_url

    message_node = etree.SubElement(root, 'message')
    message_node.text = etree.CDATA(content)

    return_sms.content = content
    
    return_sms.save()

    return root

def create_error(content, sms, err_type):
    """Create error xml
    sms can be None for now, if the sms didn't save somehow
    """

    return_error = models.ReturnError()
    return_error.sms = sms

    err_types = ('user', 'system')
    if not err_type in err_types:
        raise TypeError('Unknown error type %s' % err_type)

    root = etree.Element('error')
    root.set('type', err_type)
    root.text = content

    return_error.err_type = err_type
    return_error.text = content

    return_error.save()

    return root

# EOF

