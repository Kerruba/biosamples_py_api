from biosamples_py_api import biosamples_api


class Relations:
	def __init__(self, relations=None):
		if relations is None:
			self._relations = None
			self._cached = False
		else:
			self._relations = relations
			self._cached = True

	def derived_from(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("derivedFrom")))

	def derived_to(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("derivedTo")))

	def parent_of(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("parentOf")))

	def groups(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("groups")))

	def external_links(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("externalLinks")))

	def child_of(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("childOf")))

	def recurated_from(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("recuratedFrom")))

	def recurated_to(self):
		return self.extract_relations(biosamples_api.query_api(self.get_relation_url("recuratedTo")))

	def get_relation_url(self, type):
		if self._relations is not None and type in self._relations:
			return self._relations[type]["href"]
		else:
			return None
	
	def extract_relations(self, obj):
		if obj and "_embedded" in obj and "samplesrelations" in obj["_embedded"]:
			return [x["accession"] for x in obj["_embedded"]["samplesrelations"]]
		else:
			return None


def _test():
	relations = biosamples_api.get_sample_relations("SAMEA3473825")
	assert relations.derived_from() == ["SAMEA2629548"]
	assert relations.derived_to() == ['SAMEA3473858', 'SAMEA3473861', 'SAMEA3473849', 'SAMEA3473852', 'SAMEA3473834', 'SAMEA3473845', 'SAMEA3473821', 'SAMEA3473855', 'SAMEA3473824', 'SAMEA3473856', 'SAMEA3473837', 'SAMEA3473862', 'SAMEA3473833', 'SAMEA3473823', 'SAMEA3473848', 'SAMEA3473850', 'SAMEA3473813', 'SAMEA3473838', 'SAMEA3473842', 'SAMEA3473829', 'SAMEA3473840', 'SAMEA3473819', 'SAMEA3473817', 'SAMEA3473843', 'SAMEA3473844', 'SAMEA3473851', 'SAMEA3473814', 'SAMEA3473859', 'SAMEA3473818', 'SAMEA3473820', 'SAMEA3473846', 'SAMEA3473830', 'SAMEA3473828', 'SAMEA3473815', 'SAMEA3473857', 'SAMEA3473863', 'SAMEA3473822', 'SAMEA3473832', 'SAMEA3473860', 'SAMEA3473816', 'SAMEA3473847', 'SAMEA3473835', 'SAMEA3473839', 'SAMEA3473854', 'SAMEA3473831', 'SAMEA3473827', 'SAMEA3473826', 'SAMEA3473853', 'SAMEA3473836', 'SAMEA3473841']
	assert relations.child_of() is None
	assert relations.groups() is None
	assert relations.parent_of() is None


if __name__ == "__main__":
	_test()