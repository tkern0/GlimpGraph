import os, subprocess
badFile = True
if os.path.isfile("GlicemiaMisurazioni.csv"):
    if not open("GlicemiaMisurazioni.csv").read()[-8:] == "modified":
        badFile = False
while badFile:
    print("'GlicemiaMisurazioni.csv' does not exist or has been modified")
    print("Please add an unmodified version to the current directory")
    _ = input("Press ENTER to continue")
FNULL = open(os.devnull, 'w')
subprocess.call(["adb", "pull", "/storage/sdcard0/GlicemiaWearMisurazioni.csv"], stdout=FNULL, stderr=subprocess.STDOUT)
FNULL.close()
badFile = True
if os.path.isfile("GlicemiaWearMisurazioni.csv"):
    if not open("GlicemiaWearMisurazioni.csv").read()[-8:] == "modified":
        badFile = False
while badFile:
    print("'GlicemiaWearMisurazioni.csv' does not exist or has been modified")
    print("Please add an unmodified version to the current directory")
    _ = input("Press ENTER to continue")
open("GlicemiaMisurazioni.csv", "w").write("".join(sorted(list(set(open("GlicemiaMisurazioni.csv").readlines() + open("GlicemiaWearMisurazioni.csv").readlines())), reverse=True)))
# os.remove("GlicemiaWearMisurazioni.csv")