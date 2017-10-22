# MoneroUserScraper

------------
Update 2017-10-22 based on feedback:

So crypto currency is a tough topic to broach when talking about infosec because it's very 1. polarized and 2. filled with misinformation. The purpose of this script IS NOT to tear down monero. It's also not to pump another coin (I intentionally disclosed I support a competitor without naming it because I want people to know this). The opposite in fact. I want to help users stay protected. This would only serve to help Monero in the long run. 

The purpose of this script (as simple as it is), the article I wrote about it here https://dotnetrussell.com/index.php/2017/10/21/locating-monero-users-via-transaction-broadcasts/ and the twitter bot that posts the ips here https://twitter.com/moneroident is to just bring awareness to a fundimental issue with the current system. That is, that if you join the p2p network, and don't obfuscate your IP, you ARE broadcasting your location and that you use monero to the world. 

So I've read the concerns about my post and I'd like to clearify somethings that obviously were not made clear enough. 

1. When you connect to the p2p network there are a TON of other nodes that rebroadcast that may or may not be wallets. I'd be willing to bet though that a majority of monero daemons were started by the wallet (because it does it by default)

2. While you're connected YOU DO have to obfuscate your IP, the wallet doesn't do it by default (though they say they're fixing this in a coming release) This isn't only my opinion, it's been made clear by a number of Monero reps. 

3. The developers have already said this was a problem. So this isn't something new that I made up out of the blue. I'm simply showing that it's VERY EASY to see who is on the network. I never intended for it to be considered a new attack vector. People inferred that. I was simply writing a PoC of something that I didn't think had one yet. 

I've always stood behind my work and I still do. Please feel free to reach out to me if you have questions in regards to this. Also please feel free to reach out if you have evidence that proves I'm wrong! Anyone that knows me personally will tell you I'm the first person to claim it when I fuck up. However, I don't think I'm wrong in this case. I just don't think I'm as right as the community is making it out to be haha. 

-------------

Original Post:

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
