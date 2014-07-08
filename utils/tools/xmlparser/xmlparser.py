import os, shutil
from utils import logger
from xml.dom import minidom

def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    writer.write(indent + "<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()
    a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
          and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.nodeType is not minidom.Node.TEXT_NODE:
                node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))

class XMLParser():
    xml_file = None
    xmldom = None
    root = None
    def __init__(self, xml_file=""):
        self.xml_file = xml_file
        if self.xml_file != "":
            self.xmldom = minidom.parse(xml_file)
            self.root = self.xmldom.documentElement

    def update_param(self, task_name, param_name, param_value):
        for taskitem in self.root.getElementsByTagName("task"):
            if taskitem.getAttribute("name") == task_name:
                for paramitem in taskitem.getElementsByTagName("param"):
                    if paramitem.getAttribute("name") == param_name:
                        paramitem.setAttribute("value", param_value)
                        self.__write_xml()

    @classmethod
    def xml_copy(self, source, destination):
        shutil.copy(source, destination) 

    def __write_xml(self):
        minidom.Element.writexml = fixed_writexml
        xmlfile = open(self.xml_file, 'w')
        self.xmldom.writexml(xmlfile, addindent='' , newl='\n')
        xmlfile.close()

if __name__ == "__main__":
    pass
