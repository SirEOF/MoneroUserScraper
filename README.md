# MoneroUserScraper

It's never been a secret that the Monero client broadcasts your ip without obfuscating it when you make a transaction. Hopefully this script raises awareness.

To run the script:

Either start a monero daemon on your windows 10 box (with linux subsystem enabled) or start it on a linux box.

Then run the script with python (don't forget to sudo)

`sudo python monero_ip_scraper.py`

You should get an output like this
```
USER FOUND: xxx.xxx.xxx.xxx 
USER FOUND: xxx.xxx.xxx.xxx 
USER FOUND: xxx.xxx.xxx.xxx 
USER FOUND: xxx.xxx.xxx.xxx 
USER FOUND: xxx.xxx.xxx.xxx 
USER FOUND: xxx.xxx.xxx.xxx 
USER FOUND: xxx.xxx.xxx.xxx
SLEEPING FOR X MIN 
```
