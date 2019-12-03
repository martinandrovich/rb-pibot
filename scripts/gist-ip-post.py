#!/usr/bin/env python3

import sys
import time
import urllib
import github  # PyGithub
import subprocess

# tokens
API_TOKEN = "b2a572ae51a8307432337ce0bfe284a2fcdf6879"
GIST_TOKEN = "1d2605660e4f297205c4f94c2c7266d5"

# information
print("IP address to Gist script, v.1.0\n")

# test wifi
for num_attempts in range(5, 0, -1):

    try:
        print("Testing connection; attempts left:", num_attempts)
        urllib.request.urlopen("http://google.com")

    except urllib.error.URLError as e:
        print("No internet connection; retrying in 5 seconds...\n")
        time.sleep(5)

    else:
        print("Connection is established")
        connected = True
        break

else:
    print("Could not establish connection; exiting application")
    sys.exit()

# determine IP address
print("Retrieving IP address...")

#bash_cmd = "hostname -I | cut -d' ' -f1"
bash_cmd = "ip a"
bash_out = subprocess.check_output(["bash", "-c", bash_cmd])

# edit gist on GitHub
gh = github.Github(API_TOKEN)
gist = gh.get_gist(GIST_TOKEN)

print("Editing gist with ID:", GIST_TOKEN)
gist.edit(
    description="Raspberry Pi Zero IP address",
    files={"pi-addr": github.InputFileContent(content=bash_out.decode("utf-8"))},
)

print("Gist has been edited; exiting application")
