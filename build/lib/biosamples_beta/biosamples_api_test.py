import biosamples_py_api.biosamples_api as biosamples_api
import unittest


class SamplesExistence(unittest.TestCase):
	existing_samples = [
		'SAMEA8005918',
		'SAMEA8005168',
		'SAMEA3292100',
		'SAMEA3292102',
		'SAMN00189215',
		'SAMN02299463'
	]
	non_existing_samples = [
		'SAMEA1123123',
		'ZAMEA1234123',
		'SAMEA7112313'
	]

	def test_samples_existence(self):
		"""the biosamples api should be able to find existing samples"""
		for sample_accession in self.existing_samples:
			result = biosamples_api.get_sample(sample_accession)
			self.assertIsNotNone(result)

	def test_samples_not_exist(self):
		for sample_accession in self.non_existing_samples:
			result = biosamples_api.get_sample(sample_accession)
			self.assertIsNone(result)

	def test_samples_are_correct(self):
		"""the accession of api returned sample should be equal to the provided accession"""
		for sample_accession in self.existing_samples:
			result = biosamples_api.get_sample(sample_accession)
			self.assertEqual(sample_accession, result['accession'])

if __name__ == '__main__':
	unittest.main()

