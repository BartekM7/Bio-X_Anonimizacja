import shutil
from pprint import pprint

import pydicom as pm
import hashlib
from pydicom.errors import InvalidDicomError
import os
import csv
from pathlib import Path


with open("../profil_anonimizacji.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=";")
    profile = {tuple(int(x.strip("()"), 16) for x in rows[1].split(',')): rows[2] for rows in reader}

dummies = {
    'AE':'anonymized',
    'AS':'001D',
    'AT':b'0101',
    'CS':'anonymized',
    'DA':'19700101',
    'DS':'0',
    'DT':'19700101000000.000000',
    'FL':b'\x00\x00\x00\x00',
    'DL':b'\x00\x00\x00\x00\x00\x00\x00\x00',
    'IS':'0',
    'LO':'0',
    'LT':'0',
    'PN':'anonymized',
    'SH':'anonymized',
    'SL':b'\x00\x00\x00\x00',
    'SS':b'\x00\x00',
    'ST':'anonymized',
    'SV':b'\x00\x00\x00\x00\x00\x00\x00\x00',
    'TM':'000000.000000',
    'UC':'anonymized',
    'UI':'anonymized',
    'UL':b'\x00\x00\x00\x00',
    'UN':b'\x00',
    'UR':'0',
    'US':b'\x00\x00',
    'UT':'0',
    'UV':b'\x00\x00\x00\x00\x00\x00\x00\x00'
}

def read_dicom_file(dicom_file_path):
    dicom_file_path = os.path.abspath(dicom_file_path)
    try:
        dcm = pm.dcmread(dicom_file_path)
        return dcm
    except FileNotFoundError:
        raise ValueError(f"File '{dicom_file_path}' not found.")
    except PermissionError:
        raise ValueError(f"Insufficient permissions to read the file '{dicom_file_path}'.")
    except InvalidDicomError:
        raise ValueError(f"File '{dicom_file_path}' is not a valid DICOM file.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred while reading the DICOM file: {e}")

def anonymization_callback(ds, elem):
    if elem.tag.group == 0x7FE0:
        return
    if elem.tag.group & 0xFF00 == 0x5000:
        del ds[elem.tag]
        return
    #if elem.tag.group & 0xFF00 == 0x6000 and (elem.tag.element == 0x4000 or elem.tag.element == 0x3000): #Overlay
     #   del ds[elem.tag]
      #  return

    if (elem.tag.group, elem.tag.element) in profile.keys():
        match profile[elem.tag.group, elem.tag.element]:
            case 'D':
                ds[elem.tag].value = dummies[elem.VR]
            case 'Z':
                ds[elem.tag].value = None
            case 'X':
                del ds[elem.tag]
            case 'U':
                ds[elem.tag].value = str(int(hashlib.sha256(str(ds[elem.tag].value).encode()).hexdigest()[:24], 16))
            case _:
                print("Found unknown action code in: ", elem.tag)




def change_single_file_data(ds):
    pass
    ds.remove_private_tags()
    ds.walk(anonymization_callback)
    ds.PatientName = str(ds.PatientID[:4]) + str(ds.StudyInstanceUID[:4])



def anonymize_single_dicom_file(dicom_input_file):

    ds = read_dicom_file(dicom_input_file)

    before_name = ds.PatientName
    before_id = ds.PatientID
    before_study_instance_id = ds.StudyInstanceUID

    change_single_file_data(ds)


    return ds, before_name, before_id, before_study_instance_id, ds.PatientName

    #print(f"Anonymized DICOM file saved as: {output_file_path}")

def anonymize_single_dicom_file_and_save(dicom_input_file, dicom_output_file):
    ds, _, _, _, _ = anonymize_single_dicom_file(dicom_input_file)
    save_dicom_file(ds, dicom_output_file)

def save_dicom_file(dcm, output_file_path, name_suffix=0):
    normalized_path = str(os.path.normpath(output_file_path)) + '/' + str(dcm.PatientName) + '.'

    while os.path.exists(normalized_path + str(name_suffix)):
        name_suffix += 1

    dcm.save_as(normalized_path + str(name_suffix))

    return normalized_path + str(name_suffix)


def anonymize_dicom_directory(dicom_input_directory, output_directory):
    if not os.path.isdir(dicom_input_directory):
        raise ValueError(f"The directory '{dicom_input_directory}' is not a directory.")

    directory_name = os.path.basename(dicom_input_directory)

    full_output_directory = str(os.path.join(output_directory, directory_name + '_anonymized'))

    if os.path.exists(full_output_directory):
        raise ValueError(f"The directory '{full_output_directory}' already exists.")

    shutil.copytree(dicom_input_directory, full_output_directory)

    path = Path(full_output_directory)

    files = [str(file) for file in path.rglob('*') if file.is_file()]

    dictionary = dict()

    for file in files:
        path = None
        try:
            ds, oldname, oldid, oldstudid, newname = anonymize_single_dicom_file(file)
            if (oldname, oldid, oldstudid) not in dictionary.keys():
                dictionary[(oldname, oldid, oldstudid)] = (newname, [])
                path = save_dicom_file(ds, os.path.dirname(file))
                dictionary[(oldname, oldid, oldstudid)][1].append(path)
            else:
                path = save_dicom_file(ds, os.path.dirname(file), len(dictionary[(oldname, oldid, oldstudid)][1]))
                dictionary[(oldname, oldid, oldstudid)][1].append(path)

        except Exception as e:
            print(e.args[0])
        finally:
            if path != file:
                os.remove(file)

    pprint(dictionary)


