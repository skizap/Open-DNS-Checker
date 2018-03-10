# Open-DNS-Checker
Quick and dirty script to check if DNS server is vulnerable to DNS Amplification

## Dependencies
* ```pip install shodan```
* ```pip install configparser```

## Details
Python script that reaches out to Shodan, searches based on what you pass to ```api.search```, and reports back. Script then checks if open recursive DNS server is vulnerable and saves all matches to a txt file. Some details were purposefully obfuscated...

### Sample output
```Found 99 hosts

Found 83 vulnerable hosts

83.84% of total hosts are vulnerable to exploitation. Saving to a file for you.

[+] Done!
```