import requests
# import simplejson as json
import logging
from biosamples_py_api.relation import Relations

"""Base class to get BioSamples and BioSamplesGroup usign the BioSample API"""

__BASE_URL = "https://www.ebi.ac.uk/biosamples/api"
__DEFAULT_ENCODING = "UTF-8"


def get_sample(accession):
	url = compose_url("samples", accession)
	return query_api(url)


def get_group(accession):
	"""Get the BioSampleGroup with specific id"""
	url = compose_url("groups", accession)
	return query_api(url)


def get_group_samples(accession, keyword="*:*", sort_by="relevance", sort_order="descending", page_size=10, page=1):
	"""Get the BioSamples accessions associated with the group"""
	base_url = "{}/samples/search/findByKeywordsAndGroupsContains".format(__BASE_URL)
	base_query = "?group={accession}&keyword={keyword}".format(**locals())
	pagination = "&sortby={sort_by}&sortorder={sort_order}&pagesize={page_size}&page={page}".format(**locals())
	url = "{}{}{}".format(base_url,base_query,pagination)
	return query_api(url)


def get_sample_relations(accession):
	url = "{}/samplesrelations/{}".format(__BASE_URL, accession);
	rel = query_api(url)
	if rel is not None:
		return Relations(rel["_links"])
	return rel


def query_api(url):

	logger = logging.getLogger("url")
	logger.debug(url)
	r = requests.get(url)
	if r.status_code == 200:
		return r.json()
	else:
		return None


# return json.loads(r.content)
# return etree.fromstring(r.content, etree.XMLParser(encoding=__DEFAULT_ENCODING))


def compose_url(doc_type, accession):
	return "{}/{}/{}".format(__BASE_URL, doc_type, accession)


#
#
# def print_xml(doc):
# 	"""Print the XML document"""
# 	print(etree.tostring(doc, pretty_print=True, method="xml").decode(__DEFAULT_ENCODING))
#
#
# def sampletab_to_jsonobj(file_path):
# 	"""Convert a given sampletab file to a json matrix string"""
#
# 	import re
# 	sampletab = []
# 	with open(file_path, "r") as f:
# 		for line in f:
# 			line = line.rstrip("\n")
# 			current_line = []
# 			for word in line.split("\t"):
# 				new_word = re.sub(r"\"", "\\\"", word)
# 				current_line.append(new_word)
# 			sampletab.append(current_line)
# 	sampletab_dict = dict()
# 	sampletab_dict["sampletab"] = sampletab
# 	return sampletab_dict
#
#
# def jsonobj_to_sampletab(json_obj, file_out="sampletab.txt"):
# 	"""Write convert the provided sampletab in json format to a text file"""
# 	import os
# 	if type(json_obj) is str:
# 		obj = json.load(json_obj)
# 	else:
# 		obj = json_obj
#
# 	overwrite_choises = {"y": True, "n": False}
# 	print("Writing into {}".format(file_out))
# 	while os.path.isfile(file_out):
# 		overwrite_input = input("Output file already exists, overwrite? [y/N] ")
# 		if not (bool(overwrite_input) and overwrite_choises.get(overwrite_input.lower(), False)):
# 			file_out = input("Provide a new path to save the file: ")
# 		else:
# 			print("File {} will be overwritten".format(os.path.abspath(file_out)))
# 			break
# 	with open(file_out, "w") as fout:
# 		for line in obj["sampletab"]:
# 			fout.write("\t".join(map(str, line)))
# 			fout.write("\r\n")
#
#
# def validate_sampletab(file_path):
# 	sampletab_json_obj = sampletab_to_jsonobj(file_path)
# 	url = "https://www.ebi.ac.uk/biosamples/beta/sampletab/api/v1/json/va"
# 	json_response = submission(url, sampletab_json_obj)
# 	if json_response:
# 		if json_response["errors"]:
# 			handle_error_response(json_response)
# 		else:
# 			# TODO change the destination file name to have a _val suffix
# 			jsonobj_to_sampletab(json_response, file_path)
#
#
# def submit_sampletab(file_path, api_key):
# 	sampletab_json_obj = sampletab_to_jsonobj(file_path)
# 	url = "https://www.ebi.ac.uk/biosamples/beta/sampletab/" \
# 	      "api/v1/json/sb?apikey={}".format(api_key)
# 	json_response = submission(url, sampletab_json_obj)
# 	if json_response:
# 		if json_response["errors"]:
# 			handle_error_response(json_response)
# 		else:
# 			# TODO change the destination file name to have a _sub suffix
# 			jsonobj_to_sampletab(json_response, file_path)
#
#
# def submission(url, jsonobj):
# 	headers = {
# 		"Content-Type": "application/json",
# 		"Connection": "keep-alive"
# 	}
#
# 	r = requests.post(url, headers=headers, data=json.dumps(jsonobj))
#
# 	if r.status_code == requests.codes.ok:
# 		json_response = r.json()
# 		return json_response
# 	#     jsonobj_to_sampletab(r.json(), file_path)
# 	else:
# 		print(r.status_code)
# 		print(r.text)
#
#
# def handle_error_response(json_response):
# 	"""Handle function for error in submission response"""
# 	print(json_response["error"])
def _test():
	assert get_sample("SAMEA3473833") is not None


if __name__ == "__main__":
	_test()



