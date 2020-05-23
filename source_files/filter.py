import exiftool
from os import listdir
from os.path import join, isfile
import csv, time
from functools import reduce


# def format_path(path):
#     return "".join(["-" if char == "/" else "" if char == "." else char for char in path]) #oof this is not readable

def generate_filename(path):
    timestr=time.strftime("%Y%m%d%H%M%S")
    return "exiftool-"+timestr+".csv"

def concat_items(item1, item2):
    return item1 + ', ' + item2

def format_item(item):
    if isinstance(item, list):
        return list_to_readable_str(item)
    else:
        return item

def list_to_readable_str(lst):
    return reduce(concat_items, lst)

def generate_dict_from_exif(exif, collection_id):
    try:
        raw_cas_data = {
            "filename": exif["File:FileName"],
            "dc.title": exif["EXIF:ImageDescription"],                                       #Image Description
            "dc.identifier.other": collection_id,                            #(this is the collection number/name. Not image metadata. Will we have to go back and add individually post-upload or is there a way to add to batches?)
            "dc.rights.holder": "California Academy of Sciences", #defaulted to cal academy
            "dc.creator": exif["XMP:Creator"],                                     #Creator
            "dc.format": exif["File:FileType"],
            "dc.coverage.spatial": exif["XMP:Location"],                            #Location
            "dc.subject": exif["XMP:Subject"],                                     #Subject (list of keywords that could easily be too extensive and/or not specific enough for our purposes)
            "dc.date.created": exif["EXIF:CreateDate"],                #(date of upload to DAM) not sure if this the date u want
            "dc.description": exif["EXIF:ImageDescription"],                                 #Image Description
            "Ibss-library.taxon": "",
            "Ibss-library.commonName": "",
            "ibss-library-familyName": "",
            "ibss-library.internalNotes": "",
            "ibss-library.containerInformation": "",
            "ibss-library.physicalLocation": "",
            "Ibss-library.filename": "",
            "dc.identifier.uri": "",
            "dc.type": "",
            "dc.rights.statement": "",                            #(I’ll check with Rebekah to see if we have a statement)
            "dc.rights.status": "",
            "Ibss-library.publish": ""
        }
    except KeyError:
        print(exif["File:FileName"]+" was missing some exif data, aborting process. ")
        raw_cas_data = {}

    cas_data = dict(zip(raw_cas_data.keys(), map(format_item, raw_cas_data.values())))
    return cas_data

def generate_row(path, file, exif_extractor, csv_writer, collection_id, header=False):
    full_path = join(path, file)
    exif_data = exif_extractor.get_metadata(full_path)
    schema_data = generate_dict_from_exif(exif_data, collection_id)

    if header:
        csv_writer.writerow(schema_data.keys())

    csv_writer.writerow(schema_data.values())

def extract_exif_data_from_dir(path, collection_id, output):
    files_in_dir = [f for f in listdir(path) if isfile(join(path, f))
                        and f.lower().endswith(('.tif'))]

    #print("Debug: Found files, "+str(files_in_dir))

    with open(join(output, generate_filename(path)), "w") as output:
        with exiftool.ExifTool() as exif_extractor:
            csv_writer = csv.writer(output)

            generate_row(path, files_in_dir[0], exif_extractor, csv_writer, collection_id, True)

            for file in files_in_dir[1:]:
                generate_row(path, file, exif_extractor, csv_writer, collection_id)

if __name__ == '__main__':

    """
    Testing
    """

    extract_exif_data_from_dir("test_data/ex1", "collection_id(input)", "out")
