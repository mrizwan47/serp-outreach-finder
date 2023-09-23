import argparse
import requests
from bs4 import BeautifulSoup

def google_search(keyword):
	url = f"https://www.google.com/search?q={keyword}"
	headers = {"User-Agent": "Mozilla/5.0"}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		links = [a['href'] for a in soup.find_all('a', href=True)]
		return links
	else:
		return []

def main():
	parser = argparse.ArgumentParser(description='SERPOutreacher: \'Write for us\' finder')
	parser.add_argument('keyword', type=str, help='Keyword to search')
	args = parser.parse_args()
	results = google_search(args.keyword)
	print(results)

if __name__ == "__main__":
	main()
