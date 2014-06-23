import os
from utils import logger
from xml.dom import minidom
# from utils.tools.htmlparser import buildparser

builds_xml = os.path.realpath(os.path.join(os.path.dirname(__file__), "builds.xml"))
xmldom = minidom.parse(builds_xml)
root = xmldom.documentElement
# def new_build_check(product_name):
#     # check the last build in html, if not in xml file then it's a new build
#     last_build = buildparser.build_list(product_name.upper())[-1]
#     if not last_build in get_builds(product_name):
#         return last_build
#     else:
#         return "No New Build"

def get_builds(product_name):
    '''product_name: "sam", "rhel", '''
    product_name = product_name.lower()
    build_list = []
    product_section = root.getElementsByTagName("%s" % product_name)
    if product_section.length == 0:
        # if product not in xml file, then add it
        logger.info("Adding new product : %s to build.xml" % product_name)
        __add_product(product_name)
    else:
        # get every build in <build>XXX</build>
        for build in product_section[0].getElementsByTagName("build"):
            for node in build.childNodes:
                if node.nodeType in (node.TEXT_NODE,):
                    build_list.append(node.data)
    logger.info("All %s builds in build.xml : %s " % (product_name, build_list))
    return build_list

def add_build(product_name, build_name):
    ''' '''
    product_section = root.getElementsByTagName("%s" % product_name.lower())[0]
    build = xmldom.createTextNode('%s' % build_name)
    item = xmldom.createElement('build')
    item.appendChild(build)
    product_section.appendChild(item)
    __write_xml()

def reset_builds(product_name, build_list):
    ''' reset product builds '''
    product_section = root.getElementsByTagName("%s" % product_name.lower())[0]

    # remove all builds in product
    for build in product_section.getElementsByTagName("build"):
        product_section.removeChild(build)

    # add builds from build_list to build.xml
    for item in build_list:
        build = xmldom.createTextNode('%s' % item)
        item = xmldom.createElement('build')
        item.appendChild(build)
        product_section.appendChild(item)
    __write_xml()

def __add_product(product_name):
    item = xmldom.createElement(product_name)
    root.appendChild(item)
    __write_xml()

def __write_xml():
    minidom.Element.writexml = __fixed_writexml
    xmlfile = open(builds_xml, 'w')
    xmldom.writexml(xmlfile, addindent='' , newl='\n')
    xmlfile.close()

def __fixed_writexml(self, writer, indent="", addindent="", newl=""):
    # indent = current indentation
    # addindent = indentation to add to higher levels
    # newl = newline string
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

if __name__ == "__main__":
#     reset_builds("sam", ["build1", "build2"])
#     reset_builds("sam", buildparser.build_list("sam".upper()))
#     add_build("sam", "testbuild")
#     __add_product("sam-1.4.0")
#     add_build("sam-1.4.0", "testbuild")
#     print get_builds("sam-1.4.0")
#     print new_build_check("sam")
    pass
