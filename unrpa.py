import os
import zlib
from cPickle import loads

def extract_files(rpa_path):

    # Open the archive file.
    rpa_file = open(rpa_path, "rb")

    # Open the index file.
    index_file = open(rpa_path.replace(".rpa", ".rpi"), "rb")

    # Load the index data.
    index_data = zlib.decompress(index_file.read())
    index = loads(index_data)

    # Create a directory to extract the files into.
    extract_dir = os.path.splitext(rpa_path)[0] + "_extracted"
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    # Extract each file from the archive.
    for filename in index.keys():

        # Open the output file.
        output_file = open(os.path.join(extract_dir, filename), "wb")

        # Extract each block of data from the archive and write it to the output file.
        for offset, length in index[filename]:
            rpa_file.seek(offset)
            data = rpa_file.read(length)
            output_file.write(data)

        # Close the output file.
        output_file.close()

    # Close the archive and index files.
    rpa_file.close()
    index_file.close()

    print "Extraction complete. Files saved to '%s'." % extract_dir

# Example usage:
extract_files("images.rpa")