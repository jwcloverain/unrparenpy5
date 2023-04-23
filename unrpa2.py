import os
import zlib
import cPickle as pickle
import io

# Open the .rpa archive file.
archivef = open("images.rpa", "rb")

# Open the .rpi index file.
indexf = open("images.rpi", "rb")

# Load the index from the .rpi file.
index = pickle.loads(zlib.decompress(indexf.read()))

# Create a directory to store the extracted files.
if not os.path.exists("extracted"):
    os.makedirs("extracted")

# Iterate over each file in the index.
for fn, offsets in index.items():
    # Open the output file for writing.
    out = open(os.path.join("extracted", fn), "wb")
    # Iterate over each block of the file in the archive.
    for offset, length in offsets:
        # Seek to the start of the block in the archive.
        archivef.seek(offset)
        # Read the block from the archive.
        data = archivef.read(length)
        # Write the block to the output file.
        out.write(data)
    # Close the output file.
    out.close()

# Close the .rpa and .rpi files.
archivef.close()
indexf.close()