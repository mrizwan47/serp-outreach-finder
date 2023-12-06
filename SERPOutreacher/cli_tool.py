import csv, time, argparse, warnings
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings('ignore', category=NotOpenSSLWarning)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def extract_serp(_keyword, _output_file, _num):

	keyword = '{} "write for us"'.format(_keyword).lower()
	google_domain = 'google.com'

	s=Service(binary_path)
	driver = webdriver.Chrome(service=s, options=chrome_options)
	driver.maximize_window()
	driver.get("https://www.{}/search?q={}&num={}".format(google_domain, keyword.replace(' ', '+'), _num))
	time.sleep(3)

	thesoup = BeautifulSoup(driver.page_source, 'lxml')
	if len(driver.page_source) < 10000:
		print("You're hit by reCaptcha :(")
		driver.quit()
	else:
		driver.quit()
		results = thesoup.find_all(class_="yuRUbf")
		print("Found {} results".format(len(results)))


		with open(_output_file, 'x') as f:

			writer = csv.writer(f)
			writer.writerow([
				'rank',
				'url',
				'domain'
			])
			rank = 0
			for result in results:

				if 'tF2Cxc' in result.parent['class']:
					# Skip if the result is from People Also Ask For section
					pass
				else:
					rank = rank + 1
					url = result.find('a')['href']
					domain = urlparse(url).netloc
					
					writer.writerow([
						rank,
						url,
						domain
					])
					
		print("Export done: {}".format(_output_file))



def main():
	parser = argparse.ArgumentParser(description='SERPOutreacher: \'Write for us\' finder')
	parser.add_argument('keyword', type=str, help='Keyword to search')
	parser.add_argument('-o', '--output', type=str, help='Output file name', default='results.csv')
	parser.add_argument('-n', '--num', type=int, help='Number of results (10-100)', default=100)

	args = parser.parse_args()
	
	extract_serp(args.keyword, args.output, args.num)


if __name__ == "__main__":
	main()
