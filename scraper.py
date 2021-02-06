#%%
import urllib.request
import pandas as pd
import bs4 as bs
from datetime import datetime
import csv

def download_data(url):
   response = urllib.request.urlopen(url)
   soup = bs.BeautifulSoup(response.read())
   return soup.find('div', id='csvData').get_text()

def save_csv(myFile, csv_input):
   with myFile:
      writer = csv.writer(myFile)
      writer.writerows([x.split(';') for x in csv_input.split('\n')])

# daily scrape. At 14:00 the data is refreshed on the RIVM site
url = 'https://www.rivm.nl/coronavirus-kaart-van-nederland-per-gemeente'
csv_input = download_data(url)
save_csv(open("C:/Users/Jesse/Documents/GitHub/projects/covid19/COVID-19/RIVM_hospitalized_data/"+ datetime.today().strftime("%m-%d-%Y %H-%M") + '.csv', 'w'), csv_input)
print('done')

# %%
