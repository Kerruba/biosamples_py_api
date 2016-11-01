from .biosamples_api import *


class BioSample:
	type = "sample"

	def __init__(self, doc):
		self._doc = doc
		self.relations = []

	def get(self, prop_name):
		return self._doc[prop_name]
