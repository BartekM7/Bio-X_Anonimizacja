import pydicom as pm
from pydicom.errors import InvalidDicomError
import os

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


def anonymize_dicom(dicom_input_file, new_file_name, patient_name=None, patient_id=None, patient_birth_date=None, patient_sex=None, patient_age=None):
    #PatientName -> string
    #PatientID -> string
    # PatientBirthDate -> zapis daty "YYYYMMDD"
    # PatientSex -> "M" lub "F" inne dane daja "Other"
    # PatientAge -> zapis '000Y', gdzie 000 odpowiada wiekowi a litera jednostke np. '068Y' = 68 years

    check_if_dicom_is_correct(dicom_input_file)

    output_file_path = os.path.join(os.path.dirname(dicom_input_file), new_file_name)

    ds = pm.dcmread(dicom_input_file)

    if patient_name is not None:
        ds.PatientName = patient_name
    if patient_id is not None:
        ds.PatientID = patient_id
    if patient_birth_date is not None:
        ds.PatientBirthDate = patient_birth_date
    if patient_sex is not None:
        ds.PatientSex = patient_sex
    if patient_age is not None:
        ds.PatientAge = patient_age

    ds.save_as(output_file_path)

    print(f"Anonymized DICOM file saved as: {output_file_path}")
    #print(ds)

    return output_file_path
