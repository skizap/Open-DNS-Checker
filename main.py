import shodan
import subprocess
import configparser

# SETUP
config = configparser.ConfigParser()
config.read('key.ini')
SHODAN_API_KEY = config["shodan"]["api_key"]  # no hardcoded sensitive data around here
TOTAL_HOSTS = []
VULN_HOSTS = []


def find_hosts():
    """ Search shodan for hosts"""
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        res = api.search(YOUR SHODAN QUERY HERE!)
        for result in res['matches']:
            TOTAL_HOSTS.append(result['ip_str'])
            # print("IP: {}".format(result['ip_str']))
    except shodan.APIError as e:
        print("[-] ERROR: {}".format(e))

    print("Found {} hosts".format(len(TOTAL_HOSTS)))
    return len(TOTAL_HOSTS)


def check_hosts():
    """ 
    Check if recursive DNS server is vulnerable to exploitation.
    Command borrowed from http://openresolver.com
    """
    for i in range(len(TOTAL_HOSTS)):
        cmd = "dig +short test.openresolver.com TXT @{}".format(TOTAL_HOSTS[i])
        resp = subprocess.getoutput(cmd)
        if len(resp) > 1:
            VULN_HOSTS.append(TOTAL_HOSTS[i])

    print("Found {} vulnerable hosts".format(len(VULN_HOSTS)))
    return len(VULN_HOSTS)


def save(lst):
    with open('targets.txt', 'w+') as f:
        for entry in lst:
            f.write(entry + '\n')


def main():
    total_len = find_hosts()
    vuln_len = check_hosts()
    percent = 100 * (vuln_len / total_len)

    print("{0:.2f}% of total hosts are vulnerable to exploitation. Saving to a file for you...\n\n".format(percent))
    save(VULN_HOSTS)
    print("[+] Done!\n\n")


if __name__ == '__main__':
    main()
