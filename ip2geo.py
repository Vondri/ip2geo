from tabulate import tabulate
import argparse
import urllib3
import json
import os
import sys

if(sys.platform == "win32"):
    os.system('cls')
if(sys.platform == "linux"):
    os.system('clear')


parser = argparse.ArgumentParser(description='Getting ip address location')
parser.add_argument("-i", "--ip", required=True, help="ip to scan")
parser.add_argument("-q", "--quick", required=False , help="Print info about scanned ip (Launch without banner)", action="store_true")
args = parser.parse_args()

if args.quick==False:
    print(
    """
\033[1m\033[38;5;21m ██╗██████╗     ██████╗      ██████╗ ███████╗ ██████╗ \033[0m
\033[1m\033[38;5;27m ██║██╔══██╗    ╚════██╗    ██╔════╝ ██╔════╝██╔═══██╗\033[0m
\033[1m\033[38;5;33m ██║██████╔╝     █████╔╝    ██║  ███╗█████╗  ██║   ██║\033[0m
\033[1m\033[38;5;39m ██║██╔═══╝     ██╔═══╝     ██║   ██║██╔══╝  ██║   ██║\033[0m
\033[1m\033[38;5;45m ██║██║         ███████╗    ╚██████╔╝███████╗╚██████╔╝\033[0m
\033[1m\033[38;5;51m ╚═╝╚═╝         ╚══════╝     ╚═════╝ ╚══════╝ ╚═════╝ \033[0m
                \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mAuthor: Vondri\033[0m\033[38;5;237m [\033[38;5;54m*\033[38;5;237m]\033[0m
    """)

url = "http://ip-api.com/json/"+args.ip+"?fields=66846719"

http = urllib3.PoolManager()
res = http.request('GET', url)
data = json.loads(res.data.decode('utf-8'))

print(" \033[38;5;245mScanning ip: \033[38;5;250m" + args.ip+"\033[38;5;245m...\033[0m")
if(data["status"]=="success"):
    print(tabulate([
        ["Continent", data["continent"] + " [" + data["continentCode"] + "]"],
        ["Country", data["country"] + " [" + data["countryCode"] + "]"],
        ["Region", data["regionName"] + " [" + data["region"] + "]"],
        ["City", data["city"]],
        ["Disctrict", data["district"]],
        ["Zip code", data["zip"]],
        ["Latitute", str(data['lat'])],
        ["Longitude", str(data["lat"])],
        ["Timezone", data["timezone"]],
        ["Offset", str(data["offset"])],
        ["Currency", data["currency"]],
        ["ISP", data["isp"]],
        ["Organization", data["org"]],
        ["AS", data["as"]],
        ["AS Name", data["asname"]],
        ["Reverse DNS", data["reverse"]],
        ["Proxy, VPN or Tor", str(data["proxy"])],
        ["Hosting or data center", str(data["hosting"])]
    ], tablefmt="fancy_grid")) #fancy_frid, pretty, moinmoin