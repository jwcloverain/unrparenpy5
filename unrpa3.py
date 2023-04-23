import os
import zlib
from pickle import loads
from io import BytesIO

# Open the archive and index files for reading
archivef = open('images.rpa', 'rb')
indexf = open('images.rpi', 'rb')

# Read the index dictionary from the index file and decompress it
index = loads(zlib.decompress(indexf.read()))

# Create a directory for the extracted files, if it doesn't exist
if not os.path.exists('extracted'):
    os.makedirs('extracted')

# Loop over the files in the index dictionary and extract their data
for filename, data_offsets in index.items():
    for offset, length in data_offsets:
        # Seek to the beginning of the data within the archive
        archivef.seek(offset)

        # Read the data from the archive and write it to a file in the extracted folder
        data = archivef.read(length)
        with open(os.path.join('extracted', filename), 'ab') as outfile:
            outfile.write(data)

# Close the files
archivef.close()
indexf.close()