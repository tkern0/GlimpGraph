from datetime import date
from datetime import timedelta as td
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot as plt
import os.path
import re
from sys import argv

# Gets all data from a selected day
# Day must be in the format DD/MM/YYYY
def getDay(dir, day):
    sensor, meter = [None for i in range(96)], []
    with open(dir) as f:
        for line in f:
            if line.split(";")[1].startswith(day):
                sLine = line.split(";")
                if sLine[6] == "0":
                    # TODO: Make this list nicer for when the graph is plotted
                    meter.append({"T": getDayPart(sLine[1].split(" ")[1]),
                                  "B": safeFloat(sLine[5])})
                else:
                    sensor[getDayPart(sLine[1].split(" ")[1][:5])] = safeFloat(sLine[5])
    return sensor, meter

# Takes time inputed in the format HH.MM
# Returns which 15m section of the day it is part of
# This is used to make averages possible
def getDayPart(t):
    s = str(t).split(".")
    return int(int(s[1])/15) + int(s[0]) * 4

# Averages the values of several days
def getAverageDay(days):
    tBGL = [[] for i in range(96)]
    for day in days:
        for dPart in range(96):
            tBGL[dPart].append(day[dPart])
    fBGL = [None for i in range(96)]
    for i in range(96): fBGL[i] = meanNone(tBGL[i])
    return fBGL

# The file comes with nul characters which causes problems
# This removes them
def fixFile(dir1, dir2=None):
    if not dir2: dir2=dir1
    fi = open(dir1, 'rb')
    data = fi.read()
    fi.close()
    fo = open(dir2, 'wb')
    fo.write(data.replace(b'\x00', b''))
    fo.close()

# Coverts from mg/dL to mmoL/L
def convertMMOLL(levels):
    nLevels = []
    for i in levels:
        if i == None: nLevels.append(None)
        else: nLevels.append(i/18)
    return nLevels

# Rounds all the values in a list to 1 decimal
def roundLevels(levels):
    nLevels = []
    for i in levels:
        if i == None: nLevels.append(None)
        else: nLevels.append(round(i, 1))
    return nLevels

# Gets the mean of a list, ignoring 'None's
def meanNone(l): 
    a = [i for i in l if not i == None]
    if not a == []: return sum(a)/len(a)
    else: return None

# Coverts the given number to a float, or None if it doesn't exist
# For some reason sometimes no value is added in the file, this is to prevent the program crashing
def safeFloat(n):
    try: return float(n)
    except ValueError: return None

# Getting some starting vars
if len(argv) < 2:
    print("Input the location of 'GlicemiaMisurazioni.csv'")
    f = input("> ")
else: f = argv[1]
while not os.path.isfile(f) and os.path.basename(f) == "GlicemiaMisurazioni.csv":
    print("Incorrect file or file does not exist")
    f = input("GlicemiaMisurazioni.csv location: ")
fixFile(f)
print("Do you want to convert levels to mmol/L? [Y/N] ")
mi = input("> ").lower()
while mi not in ("y", "n", "yes", "no"):
    print("Invalid input. Please enter 'Y' or 'N'")
    print("Do you want to convert levels to mmol/L? [Y/N] ")
    mi = input("> ").lower()
mmolL = mi in ("y", "yes")
allowedIn = re.compile("^([0-9]{1,2}\\/[0-9]{1,2}\\/([0-9]{2}|[0-9]{4})|last[0-9]+|q|quit)$", re.IGNORECASE)
currentDay = date.today()
print("Input a date, in the format DD/MM/YYYY, to get BGLs from that date")
print("Input 'last[x]', where '[x]' is any positive interger, to get an average of the last '[x]' days")
print("Input 'Q' or 'Quit' to quit")
# Main loop
while True:
    day = input("> ").lower()
    if allowedIn.match(day):
        if day in ("q", "quit"): break
        elif day.startswith("last"):
            checkDays, levels = [], []
            firstDay = currentDay - td(days=int(day[4:]))
            for i in range((currentDay-firstDay).days + 1): checkDays.append((firstDay + td(days=i)).strftime("%d/%m/%Y"))
            for i in checkDays:
                s, m = getDay(f, i)
                levels.append(s)
            plt.title("Average of {} to {}".format(firstDay, currentDay))
            plt.xlabel("Part of day (1 = 15m)")
            if mmolL:
                plt.ylabel("BGL (mmol/L)")
                avLevels = roundLevels(convertMMOLL(getAverageDay(levels)))
            else:
                plt.ylabel("BGL (mg/dL)")
                avLevels = roundLevels(getAverageDay(levels))
            plt.plot(0, meanNone(s), "wo")
            plt.plot(96, meanNone(avLevels), "wo")
            plt.plot(avLevels, "r-")
        else:
            sDay = day.split("/")
            fDay = sDay[0].zfill(2) + "/" + sDay[1].zfill(2) + "/" + str("20" if len(sDay[2]) == 2 else "") + sDay[2]
            s, m = getDay(f, fDay)
            plt.title(fDay)
            plt.xlabel("Part of day (1 = 15m)")
            if mmolL:
                s = roundLevels(convertMMOLL(s))
                ml = roundLevels(convertMMOLL([i["B"] for i in m]))
                plt.ylabel("BGL (mmol/L)")
            else:
                s = roundLevels(s)
                ml = roundLevels([i["B"] for i in m])
                plt.ylabel("BGL (mg/dL)")
            plt.plot(s, "r-")
            plt.plot(0, meanNone(s), "wo")
            plt.plot(96, meanNone(s), "wo")
            plt.plot([i["T"] for i in m], ml, "ro")
        plt.show()
    else: print("Invalid input")
