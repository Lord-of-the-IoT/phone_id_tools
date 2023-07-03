#just for parsing web stuff to compile database of MCCs and MNCs
"""import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

url="https://mcc-mnc-list.com/list"
response = requests.get(wikiurl)
soup = BeautifulSoup(response.text, 'html.parser')
tables=soup.find_all('table',{'class':"wikitable"})

def parse_table(table):
	df=pd.read_html(str(table))
	# convert list to dataframe
	df=pd.DataFrame(df[0])
	return df


test = parse_table(tables[0])
national = parse_table(tables[1])
transnat = parse_table(tables[2])

test = test.drop(["MNC", "Brand", "Status", "Bands (MHz)", "References and notes"], axis=1)
national = national.drop(["ISO 3166", "Mobile network codes", "National MNC authority", "Remarks"], axis=1)
transnat = transnat.drop(["MNC", "Status", "Bands (MHz)", "References and notes"], axis=1)

#print(transnat.to_string())


codes = "print({"
for i in range(test.shape[0]):
	codes += f'"{test.loc[i][0]:03}": "{test.loc[i][1]}",'
for i in range(national.shape[0]):
	codes += f'"{national.loc[i][0]:03}": "{national.loc[i][1]}",'
codes += "})"

codes  = eval(codes)



#https://www.emnify.com/iot-glossary/iccid-number
#https://onomondo.com/blog/iccid-number-explained/
#https://www.itu.int/en/ITU-T/inr/forms/Pages/iin.aspx
