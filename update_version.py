import datetime

# ชื่อไฟล์ที่จะเก็บข้อมูลเวอร์ชัน
version_file = "include/version.h"

# อ่านข้อมูลเวอร์ชันปัจจุบัน
try:
    with open(version_file, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

# หาบรรทัดที่เก็บเลขเวอร์ชัน และเพิ่มค่าขึ้น 1
new_version = 1
updated = False
for i, line in enumerate(lines):
    if "#define BUILD_NUMBER" in line:
        try:
            current_version = int(line.split()[2])
            new_version = current_version + 1
            lines[i] = f'#define BUILD_NUMBER {new_version}\n'
            updated = True
        except (ValueError, IndexError):
            pass # ถ้าหาไม่เจอ หรือแปลงค่าไม่ได้ ให้ใช้ค่าเริ่มต้น

# ถ้าไม่เจอ ให้เพิ่มบรรทัดใหม่
if not updated:
    lines.append(f'#define BUILD_NUMBER {new_version}\n')

# เพิ่มวันที่และเวลาที่ Build
date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if "#define BUILD_DATE" not in "".join(lines):
    lines.append(f'#define BUILD_DATE "{date_time}"\n')
else:
    for i, line in enumerate(lines):
        if "#define BUILD_DATE" in line:
            lines[i] = f'#define BUILD_DATE "{date_time}"\n'
            break

# เขียนไฟล์เวอร์ชันใหม่
with open(version_file, "w") as f:
    f.writelines(lines)

print(f"✅ Version updated to: {new_version} on {date_time}")