import zipfile

def zip_extractor(compressed_filepath, dest_path):
    with zipfile.ZipFile(compressed_filepath, 'r') as archive:
        archive.extractall(dest_path)
