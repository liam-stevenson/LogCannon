# LogCannon

## What's this for?

Ever wanted to replay logs to test certain in an ingestion pipeline or to load test a pipeline/SIEM? 
LogCannon allows you to get BOTSv1 data (https://github.com/splunk/botsv1), clean it and replay it with current time stamps at a pace that you want.

Disclaimer: I am a bad Python developer, so review code at your own peril!

## Supported Logs

* iis (use snipSize of 19)
* fgt_utm (use snipSize of 15)
* fgt_event (use snipSize of 15)
* fgt_traffic (use snipSize of 15)

## cleaner.py

So far it seems that that it's more efficent to have the data cleaned first so you just have the log with the missing (or replaced) timestamp. 

Run cleaner.py with the --type option to specific which file to clean and --snipSize to define where the time stamp ends. This will result in a log file made with the type as the name 
So far only support s Botsv1 logs where the timestamp is at the start:

*usage: cleaner.py [-h] [--logtype LOGTYPE] [--snipSize SNIPSIZE]*

**Example:**
*python3 cleaner.py --logtype fgt_utm --snipSize 15*

## cannon.py
After cleaning you can use the cannon.py to run the cannon with your new file log much faster than if you converted at the time.

*usage: app.py [-h] [--type TYPE] [--amount AMOUNT] [--frequency FREQUENCY] [--outfile OUTFILE] [--infile INFILE]*

**Example:**
*python3 app.py --type=iis --frequency 1 --amount 5 --outfile newiis.log --infile target.log*

## TODO 
1. Tidy up the variable names!
2. Support more file types
3. If the event is CEF, change the values of the date and time fields
