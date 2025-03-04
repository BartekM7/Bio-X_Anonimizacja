import pydicom as pm
from pydicom.errors import InvalidDicomError
import os
from pydicom import uid
import uuid

def check_if_dicom_is_correct(dicom_file_path):
    dicom_file_path = os.path.abspath(dicom_file_path)
    try:
        dcm = pm.dcmread(dicom_file_path, stop_before_pixels=True)
    except FileNotFoundError:
        raise ValueError(f"File '{dicom_file_path}' not found.")
    except PermissionError:
        raise ValueError(f"Insufficient permissions to read the file '{dicom_file_path}'.")
    except InvalidDicomError:
        raise ValueError(f"File '{dicom_file_path}' is not a valid DICOM file.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred while reading the DICOM file: {e}")


def anonymize_dicom(dicom_input_file, output_file_path, patient_name="Anonymous", patient_id=None, patient_birth_date="20200202"):
    #PatientName -> string; jesli nie wpiszesz to bedzie "Anonymous"
    #PatientID -> string; jesli nie wpiszesz generuje losowy numer
    # PatientBirthDate -> zapis daty "YYYYMMDD"; jesli nie wpiszesz to bedzie "20200202"

    check_if_dicom_is_correct(dicom_input_file)

    ds = pm.dcmread(dicom_input_file)

    ds.PatientName = patient_name
    ds.PatientBirthDate = patient_birth_date

    if patient_id is not None:
        ds.PatientID = patient_id
    else:
        ds.PatientID= str(uuid.uuid4())

    ds.StudyInstanceUID = pm.uid.generate_uid()

    ds.save_as(output_file_path)

    #print(f"Anonymized DICOM file saved as: {output_file_path}")
