import re
import sys
import xml.sax

class NoteHandler(xml.sax.ContentHandler):
    def __init__(self, output_file):
        self.inNote = False
        self.inTitle = False
        self.inContent = False

        self.title = ""
        self.content = ""

        self.writer = open(output_file, "w")

    def startElement(self, tag, attributes):
        #print tag
        if tag == "note":
            self.inNote = True
        elif self.inNote:
            if tag == "title":
                self.inTitle = True
            elif tag == "content":
                self.inContent = True

    def endElement(self, tag):
        if tag == "note":
            self.inNote = False

            # just grit your teeth and bear the next 10 lines or so, evernote's HTML-inside-note-content formatting is 
            #  annoyingly inconsistent, and I don't care to spend a lot of time understanding it :)

            # preserve line breaks     
            self.content = self.content.replace("<br", "\n<br")
            self.content = self.content.replace("<div", "\n<div")
            self.content = self.content.replace("<span", "\n<span")

            # remove the HTML for now
            self.content = re.sub("<.*?>", "", self.content)

            # escape-quote any actual quotation marks
            self.title = self.title.replace('"', '""')
            self.content = self.content.replace('"', '""')
            
            # debugging printfs :)
            #print "***"
            #print (self.title + ":" + self.content).encode("utf8")
            #print "***"

            self.writer.write(("\"%s\";\"%s\"\n" % (self.title, self.content)).encode("utf8"))

            self.title = self.content = ""
            
        elif self.inNote:
            if tag == "title":
                self.inTitle = False
            elif tag == "content":
                self.inContent = False

    def characters(self, content):
        #print "***" + content
        if self.inTitle:
            self.title = content
        elif self.inContent:
            self.content += content


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python enote2anki.py <filename.enex>"
        sys.exit(0)
    
    input_file = sys.argv[1]
    output_file = input_file.replace(".enex", ".txt")

    parser = xml.sax.make_parser()

    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = NoteHandler(output_file)
    parser.setContentHandler(Handler)

    parser.parse(input_file)

    print "Output written to %s" % output_file