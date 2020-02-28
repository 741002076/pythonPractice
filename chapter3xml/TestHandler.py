from xml.sax import ContentHandler


class TestHandler(ContentHandler):

    def startElement(self,name,attrs):
        print(name,attrs.keys())