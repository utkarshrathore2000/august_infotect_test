import requests
from bs4 import BeautifulSoup


def scrap_data():
	"""
	This function is used to scrap all the heading of the Crawler Test Site
	"""
	data = {"sites_heading_name":[]}
	
	url = "https://crawler-test.com/"
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, "html.parser")
		all_rows = soup.findAll('div', class_='row side-collapsed')
		for rows in all_rows:
			column = rows.findAll('div', class_='large-4 columns')
			for item in column:
				name = item.findAll('h3')[0].text
				data['sites_heading_name'].append(name)
	return data


def save_data_to_file(data, filename):
	"""
	This function is used to save the data in the text file
	"""

	with open(filename, "w") as file:
		for key, value in data.items():
			file.write(f"{key}: {value}\n")

data = scrap_data()
save_data_to_file(data, "crawler_test_site_data.txt")