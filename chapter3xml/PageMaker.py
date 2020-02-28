from xml.sax import ContentHandler, parse


class PageMaker(ContentHandler):
    passThrough = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passThrough = True
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html><head>\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head><body>\n')
        elif self.passThrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key, val))
            self.out.write('>')

    def endElement(self, name):
        if name == 'page':
            self.passThrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passThrough:
            self.out.write('</{}>'.format(name))

    def characters(self, content):
        if self.passThrough: self.out.write(content)


parse('website.xml', PageMaker())
