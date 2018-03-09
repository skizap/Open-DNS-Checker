# Open-DNS-Checker
Quick and dirty script to check if DNS server is vulnerable to DNS Amplification

## Dependencies
* ```pip install shodan```
* ```pip install configparser```

## Details
Quick python that reaches out to Shodan, searches based on what you pass to ```api.search```, and reports back. Script then checks if open recursive DNS server is vulnerable and saves all matches to a txt file. Some details were purposefully obfuscated...
