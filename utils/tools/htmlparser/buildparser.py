"""
parse all builds from HTML into a list
"""
import urllib
from utils import logger
from sgmllib import SGMLParser

class BuildParser(SGMLParser):
	build_url = ""
	def reset(self):
		self.is_a = 0
		self.build_lists = []
		SGMLParser.reset(self)

	def start_a(self, attrs):
		self.is_a = 1

	def end_a(self):
		self.is_a = 0

	def handle_data(self, data):
		if self.is_a and self.is_build(data):
			logger.debug("add %s " % data)
			self.build_lists.append(data)

# 	def __get_build_list(self):
# 		"""Parse and return all builds"""
# 		return ", ".join(self.build_lists)

	def __get_html_source(self):
		"""Accept a url and return html source"""
		sock = urllib.urlopen(self.build_url)
		htmlSource = sock.read()
		sock.close()
		# logger.debug(htmlSource)
		return htmlSource

	def parse(self):
		self.feed(self.__get_html_source())
		self.close()
		return self.build_lists

	def is_build(self, data):
		raise NotImplementedError, "Cannot call abstract method"

class SAMBuildParser(BuildParser):
	"""  """
	build_url = "http://download.devel.redhat.com/devel/candidate-trees/SAM/"
	def is_build(self, data):
		if data.startswith('SAM'):
			return 1
		else:
			return 0

class RHELBuildParser(BuildParser):
	"""  """
	build_url = "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/"
	def is_build(self, data):
		if data.startswith('RHEL'):
			return 1
		else:
			return 0

def build_list(product_name):
	parserName = "%sBuildParser" % product_name
	parser = globals()[parserName]()
	return parser.parse()

if __name__ == "__main__":
	logger.debug(build_list("SAM"))
	logger.debug(build_list("RHEL"))
