import sys
import aiohttp
import asyncio
import re

class Proxies:
	def __init__(self, proxy_url_list=[
		"https://www.us-proxy.org",
		"https://www.socks-proxy.net",
		"https://proxyscrape.com/free-proxy-list",
		"https://www.proxynova.com/proxy-server-list/",
		"https://proxybros.com/free-proxy-list/",
		"https://proxydb.net/",
		"https://spys.one/en/free-proxy-list/"
	]) -> None:
		self.proxy_url_list = proxy_url_list

	async def fetch_proxies_from_url(self, url) -> list:
		async with aiohttp.ClientSession() as session:
			try:
				async with session.get(url) as response:
					response_text = await response.text()
					ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", response_text)
					print(f"[*] Fetched {len(ip_addresses)} proxy IP addresses from {url}")
					return ip_addresses
			except Exception as error:
				print(f"[!] Error fetching proxy IP addresses from {url}: {error}")
				return []

	async def fetch_all_proxies(self) -> list:
		fetch_tasks = [self.fetch_proxies_from_url(url) for url in self.proxy_url_list]
		proxy_ip_lists = await asyncio.gather(*fetch_tasks)
		all_proxy_ips = [ip for sublist in proxy_ip_lists for ip in sublist]
		print(f"[*] Total proxy IP addresses fetched: {len(all_proxy_ips)}")
		return all_proxy_ips



if __name__ == '__main__':
	exit("Cannot execute '" + sys.argv[0] + "' without m3ddos!")
