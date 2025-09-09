import os
import sys

# File to read version info from
version_file = "include/version.h"

# Check if the version file exists
if not os.path.exists(version_file):
    print("⛔ Error: version.h not found.")
    sys.exit(1)

# Read the version info
build_number = "N/A"
build_date = "N/A"
with open(version_file, "r") as f:
    for line in f:
        if "#define BUILD_NUMBER" in line:
            try:
                build_number = line.split()[2].strip()
            except IndexError:
                pass
        elif "#define BUILD_DATE" in line:
            try:
                build_date = line.split('"')[1].strip()
            except IndexError:
                pass

# Print the message
print("--------------------------------------------------")
print(f"✅ Firmware Uploaded Successfully!")
print(f"   Build Number: {build_number}")
print(f"   Build Date:   {build_date}")
print("--------------------------------------------------")