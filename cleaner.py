import json
import argparse
import sys
import requests
import os 
import gzip



def download_file(url,logtype):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(logtype, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: 
                    f.write(chunk)
    return logtype


def cleanLogs(logtype, snipSize):
    inFilename = "botsv1." + logtype + ".json"
    outFilename = logtype + ".log"
    print("[+] Determining if specified rounds exist")
    try:

        if os.path.isfile(inFilename):
            print("[+] Munitions, skipping to cleaning")

        else:
            url = "https://s3.amazonaws.com/botsdataset/botsv1/json-by-sourcetype/botsv1." + logtype + ".json.gz"
            logtypename = "botsv1." + logtype + ".json.gz"
            download_file(url, logtypename)

            print("[+] Got file botsv1." + logtype + ".json.gz")
            print("[+] Unpacking file")
            try:
                f=gzip.open(logtypename,"rb")
                file_content=f.read()
                with open("botsv1." + logtype + ".json", "wb") as flump:
                    flump.write(file_content)
                print("[+] Removing compressed file " + logtypename)

                os.remove(logtypename)



            except Exception as e:
                print("[!] Could not extract the munitions " + e)
    except Exception as e:
        print(e) 
        sys.exit()
    
    
    try:
        print("[+] Trimming the time stamp in " + inFilename)
        ammoCrate = open(inFilename, "r")
        for shell in ammoCrate:
            log = json.loads(shell)
            if "result" in log:
                logmessage = log["result"]["_raw"].rstrip()
                print(logmessage[snipSize:], file=open(outFilename, "a")) 
        print("[+] Removing " + inFilename)
        os.remove(inFilename)

    except:
        print("nope")
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--logtype", help="the sourcetype you wish to convert")
    parser.add_argument("--snipSize", help="Specify where the timestamp ends")
    args = parser.parse_args()
    print("[+] Starting the botsCannon prefiring squence")
    cleanLogs(args.logtype, int(args.snipSize))
    print("[+] botsCannon ready to fire " + args.logtype)
