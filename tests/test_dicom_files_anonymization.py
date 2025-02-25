from unittest import TestCase
import pydicom as pm
from dicom_files_anonymization import anonymize_dicom
import os

class TestDICOMAnonymization(TestCase):

    def test_anonymize_dicom_check_if_changes_data_as_provided(self):
        test_filename = r"files_for_tests\2\1\I00001"
        new_filename = r"files_for_tests\2\1\Test"
        try:
            anonymize_dicom(test_filename, new_filename,
                                               "Anonymous", "11111", "20200203")
            ds_anon = pm.dcmread(new_filename)

            self.assertEqual("Anonymous", ds_anon.PatientName)
            self.assertEqual("11111", ds_anon.PatientID )
            self.assertEqual("20200203", ds_anon.PatientBirthDate)

        finally:
            os.remove(new_filename)

    def test_anonymize_dicom_check_if_changes_path_name_as_provided(self):
        test_filename = r"files_for_tests\2\1\I00001"
        new_filename = r"files_for_tests\2\1\Test"
        try:
            anonymize_dicom(test_filename, new_filename,)

            self.assertEqual(r"files_for_tests\2\1\Test", new_filename)

        finally:
            os.remove(new_filename)

    def test_anonymize_dicom_check_if_leaves_data_if_not_provided(self):
        new_filename = r"files_for_tests\2\1\Test"
        test_filename = r"files_for_tests\2\1\I00001"

        try:
            anonymize_dicom(test_filename, new_filename)

            ds_anon = pm.dcmread(new_filename)

            self.assertEqual("Anonymous", ds_anon.PatientName)
            self.assertEqual("20200202", ds_anon.PatientBirthDate)
        finally:
            os.remove(new_filename)
