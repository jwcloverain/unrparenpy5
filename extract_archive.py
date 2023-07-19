import sys
import os
import zlib
import random
import glob
from cPickle import loads

def extract_archive(archive_path, index_path, output_dir):
    # Load the index file
    with open(index_path, "rb") as index_file:
        index = loads(zlib.decompress(index_file.read()))

    # Open the archive file
    with open(archive_path, "rb") as archive_file:
        # Iterate over each file in the index
        for filename, blocks in index.items():
            # Create the output directory if it doesn't exist
            output_file_path = os.path.join(output_dir, filename)
            output_directory = os.path.dirname(output_file_path)
            
            try:
                os.makedirs(output_directory)
            except OSError:
                pass

            # Open the output file for writing
            with open(output_file_path, "wb") as output_file:
                # Iterate over each block of the file
                for offset, length in blocks:
                    # Seek to the offset in the archive file
                    archive_file.seek(offset)

                    # Read the data block
                    data = archive_file.read(length)

                    # Write the data block to the output file
                    output_file.write(data)

            print "Extracted {} to {}".format(filename, output_file_path)

# Usage: extract_archive.py <archive_file_path> <index_file_path> <output_directory>
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Usage: extract_archive.py <archive_file_path> <index_file_path> <output_directory>"
        sys.exit(1)

    archive_path = sys.argv[1]
    index_path = sys.argv[2]
    output_dir = sys.argv[3]

    extract_archive(archive_path, index_path, output_dir)