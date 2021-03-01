import requests
import urllib.request
import hashlib

"""
Written for Python 3

Script to scrape the current latest version of lynis from cisofy.com, download
the file to disk and then verify the checksum
"""

destination = "/ansible/static_files/lynis-latest.tar.gz"

# Scrape downloads page and get the file
response = requests.get('https://cisofy.com/downloads/lynis/')
contents = str(response.content)
page_contents = contents.split('.tar.gz" class="button-green button-small inline left"')
filename = page_contents[0].split('https://downloads.cisofy.com/lynis/')
download_file = "https://downloads.cisofy.com/lynis/" + filename[1] + ".tar.gz"
urllib.request.urlretrieve(download_file, destination)
print("Downloaded " + filename[1] + " version, written to " + destination)

# Extract the sha256 hash from the website
sha_sum_begin = page_contents[1].split('SHA256 hash: ')

# Get the sha256 hash of the file
sha256_hash = hashlib.sha256()
with open(destination,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)

# Produce output to the user
if sha256_hash.hexdigest() == sha_sum_begin[1][:64]:
    print("Hash checks out, file is good!")
else:
    print("The hash didn't match, double check https://cisofy.com/downlaods/lynis/ page for more details")
