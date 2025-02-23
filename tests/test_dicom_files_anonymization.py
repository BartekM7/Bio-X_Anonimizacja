from unittest import TestCase
import pydicom as pm
from dicom_files_anonymization import anonymize_dicom
import os

class TestDICOMAnonymization(TestCase):

    def test_anonymize_dicom_check_if_changes_data_as_provided(self):
        test_filename = r"files_for_tests\2\1\I00001"
        new_filename = "Test"
        try:
            output_file_path = anonymize_dicom(test_filename, new_filename,
                                               "A", "A", "20200202", "M", '068Y')
            ds_anon = pm.dcmread(output_file_path)

            self.assertEqual("A", ds_anon.PatientName)
            self.assertEqual("A", ds_anon.PatientID )
            self.assertEqual("20200202", ds_anon.PatientBirthDate)
            self.assertEqual("M", ds_anon.PatientSex)
            self.assertEqual('068Y', ds_anon.PatientAge)

        finally:
            os.remove(output_file_path)

    def test_anonymize_dicom_check_if_changes_path_name_as_provided(self):
        test_filename = r"files_for_tests\2\1\I00001"
        new_filename = "Test"
        try:
            output_file_path = anonymize_dicom(test_filename, new_filename,)

            self.assertEqual(r"files_for_tests\2\1\Test", output_file_path)

        finally:
            os.remove(output_file_path)

    def test_anonymize_dicom_check_if_leaves_data_if_not_provided(self):
        new_filename = "Test"
        test_filename = r"files_for_tests\2\1\I00001"

        try:
            output_file_path = anonymize_dicom(test_filename, new_filename)

            ds_anon = pm.dcmread(output_file_path)

            self.assertEqual("Anonymous", ds_anon.PatientName)
            self.assertEqual("90012514477", ds_anon.PatientID)
            self.assertEqual("19700101", ds_anon.PatientBirthDate)
            self.assertEqual("M", ds_anon.PatientSex)
            self.assertEqual('032Y', ds_anon.PatientAge)
        finally:
            os.remove(output_file_path)

