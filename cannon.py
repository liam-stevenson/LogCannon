import json
from datetime import datetime
import time
import argparse


def magazineMaker(ammoCrate: list, size: int):
    for start in range(0, len(ammoCrate), size):
        yield ammoCrate[start:start + size]
     

def createLogCrate(sourcetype):
    
    if sourcetype == "iis":
        ammoCrate = open(args.infile, "r")
        clean_ammo = list()
        for shell in ammoCrate:
            clean_ammo.append(shell)
            timestampformat = "%Y-%m-%d %H:%M:%S"

    if "fgt" in sourcetype:
        ammoCrate = open(args.infile, "r")
        clean_ammo = list()
        for shell in ammoCrate:
            clean_ammo.append(shell)
            timestampformat = "%b %I %d - %H:%M:%S"

    while True:
        unloadMagazine(clean_ammo, int(args.amount), int(args.frequency), timestampformat)

def unloadMagazine(clean_ammo, clipSize, fireRate, timestampformat):
    for lawg in list(magazineMaker(clean_ammo, clipSize)):
            for thing in lawg:
                now = datetime.now()
                timestamp = now.strftime(timestampformat)
                newlogs = timestamp + thing 
                print(newlogs.strip('\n'), file=open(args.outfile, "a"))
            time.sleep(fireRate)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="the sourcetype you wish to fire")
    parser.add_argument("--amount", help="the the amount of logs per write you want to write per round")
    parser.add_argument("--frequency", help="The frequency you want to write the amount. Recommended to simulate EPS that 1 is used, however might lead to performace issues")
    parser.add_argument("--outfile", help="Where to write the file to")
    parser.add_argument("--infile", help="Where to write the file to")

    args = parser.parse_args()
    createLogCrate(args.type)
        
