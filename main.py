import os
from time import sleep

class Tool:
	def __init__(self):
		self.country_code = {'Test network': '001', 'Internal use': '999', 'Abkhazia': '289', 'Afghanistan': '412', 'Albania': '276', 'Algeria': '603', 'American Samoa (United States of America)': '544', 'Andorra': '213', 'Angola': '631', 'Anguilla (United Kingdom)': '365', 'Antigua and Barbuda': '344', 'Argentina': '722', 'Armenia': '283', 'Aruba': '363', 'Norfolk Island': '505', 'Austria': '232', 'Azerbaijan': '400', 'BBahamas': '364', 'Bahrain': '426', 'Bangladesh': '470', 'Barbados': '342', 'Belarus': '257', 'Belgium': '206', 'Belize': '702', 'Benin': '616', 'Bermuda': '350', 'Bhutan': '402', 'Bolivia': '736', 'Sint Maarten': '362', 'Bosnia and Herzegovina': '218', 'Botswana': '652', 'Brazil': '724', 'British Indian Ocean Territory (United Kingdom)': '995', 'British Virgin Islands (United Kingdom)': '348', 'Brunei': '528', 'Bulgaria': '284', 'Burkina Faso': '613', 'Burundi': '642', 'Cambodia': '456', 'Cameroon': '624', 'Canada': '302', 'Cape Verde': '625', 'Cayman Islands (United Kingdom)': '346', 'Central African Republic': '623', 'Chad': '622', 'Chile': '730', 'China': '461', 'Colombia': '732', 'Comoros': '654', 'Congo': '629', 'Cook Islands (Pacific Ocean)': '548', 'Costa Rica': '712', 'Croatia': '219', 'Cuba': '368', 'Cyprus': '280', 'Czech Republic': '230', 'Democratic Republic of the Congo': '630', 'Denmark (Kingdom of Denmark)': '238', 'Djibouti': '638', 'Dominica': '366', 'Dominican Republic': '370', 'East Timor': '514', 'Ecuador': '740', 'Egypt': '602', 'El Salvador': '706', 'Equatorial Guinea': '627', 'Eritrea': '657', 'Estonia': '248', 'Ethiopia': '636', 'Falkland Islands (United Kingdom)': '750', 'Faroe Islands (Kingdom of Denmark)': '288', 'Fiji': '542', 'Finland': '244', 'France': '208', 'French Guiana (France)': '742', 'French Indian Ocean Territories (France)': '647', 'French Polynesia (France)': '547', 'Gabon': '628', 'Gambia': '607', 'Georgia': '282', 'Germany': '262', 'Ghana': '620', 'Gibraltar (United Kingdom)': '266', 'Greece': '202', 'Greenland (Kingdom of Denmark)': '290', 'Grenada': '352', 'Saint Martin (France)': '340', 'United States of America': '316', 'Guatemala': '704', 'United Kingdom': '235', 'Guinea': '611', 'Guinea-Bissau': '632', 'Guyana': '738', 'Haiti': '372', 'Honduras': '708', 'Hong Kong': '454', 'Hungary': '216', 'Iceland': '274', 'India': '406', 'Indonesia': '510', 'Iran': '432', 'Iraq': '418', 'Ireland': '272', 'Palestine': '425', 'Italy': '222', 'Ivory Coast': '612', 'Jamaica': '338', 'Japan': '441', 'Jordan': '416', 'Kazakhstan': '401', 'Kenya': '639', 'Kiribati': '545', 'Korea, North': '467', 'Korea, South': '450', 'Kosovo': '221', 'Kuwait': '419', 'Kyrgyzstan': '437', 'Laos': '457', 'Latvia': '247', 'Lebanon': '415', 'Lesotho': '651', 'Liberia': '618', 'Libya': '606', 'Liechtenstein': '295', 'Lithuania': '246', 'Luxembourg': '270', 'Macau': '455', 'North Macedonia': '294', 'Madagascar': '646', 'Malawi': '650', 'Malaysia': '502', 'Maldives': '472', 'Mali': '610', 'Malta': '278', 'Marshall Islands': '551', 'Mauritania': '609', 'Mauritius': '617', 'Mexico': '334', 'Micronesia, Federated States of': '550', 'Moldova': '259', 'Monaco': '212', 'Mongolia': '428', 'Montenegro': '297', 'Montserrat (United Kingdom)': '354', 'Morocco': '604', 'Mozambique': '643', 'Myanmar': '414', 'Namibia': '649', 'Nauru': '536', 'Nepal': '429', 'Netherlands (Kingdom of the Netherlands)': '204', 'New Caledonia': '546', 'New Zealand': '530', 'Nicaragua': '710', 'Niger': '614', 'Nigeria': '621', 'Niue': '555', 'Norway': '242', 'Oman': '422', 'Pakistan': '410', 'Palau': '552', 'Panama': '714', 'Papua New Guinea': '537', 'Paraguay': '744', 'Peru': '716', 'Philippines': '515', 'Poland': '260', 'Portugal': '268', 'Puerto Rico (United States of America)': '330', 'Qatar': '427', 'Romania': '226', 'Russian Federation': '250', 'Rwanda': '635', 'Saint Helena, Ascension and Tristan da Cunha': '658', 'Saint Kitts and Nevis': '356', 'Saint Lucia': '358', 'Saint Pierre and Miquelon': '308', 'Saint Vincent and the Grenadines': '360', 'Samoa': '549', 'San Marino': '292', 'São Tomé and Príncipe': '626', 'Saudi Arabia': '420', 'Senegal': '608', 'Serbia': '220', 'Seychelles': '633', 'Sierra Leone': '619', 'Singapore': '525', 'Slovakia': '231', 'Slovenia': '293', 'Solomon Islands': '540', 'Somalia': '637', 'South Africa': '655', 'South Sudan': '659', 'Spain': '214', 'Sri Lanka': '413', 'Sudan': '634', 'Suriname': '746', 'Swaziland': '653', 'Sweden': '240', 'Switzerland': '228', 'Syria': '417', 'Taiwan': '466', 'Tajikistan': '436', 'Tanzania': '640', 'Thailand': '520', 'Togo': '615', 'Tokelau': '554', 'Tonga': '539', 'Trinidad and Tobago': '374', 'Tunisia': '605', 'Turkey': '286', 'Turkmenistan': '438', 'Turks and Caicos Islands': '376', 'Tuvalu': '553', 'Uganda': '641', 'Ukraine': '255', 'United Arab Emirates': '424', 'United Arab Emirates (Abu Dhabi)': '430', 'United Arab Emirates (Dubai)': '431', 'United States Virgin Islands': '332', 'Uruguay': '748', 'Uzbekistan': '434', 'Vanuatu': '541', 'Venezuela': '734', 'Vietnam': '452', 'Wallis and Futuna': '543', 'Yemen': '421', 'Zambia': '645', 'Zimbabwe': '648'}

	def error(self, reason):
		print('\n\n        \033[1;31m[!] '+reason+'\033[0m')
		sleep(3)

	def banner(self):
		os.system('clear')
		print("                \033[1;34m.______    __    __    ______   .__   __.  _______    .__   __.  __    __  .___  ___. .______    _______ .______         .___________.  ______     ______    __          _______.\033[0m")
		print("                \033[1;34m|   _  \\  |  |  |  |  /  __  \\  |  \\ |  | |   ____|   |  \\ |  | |  |  |  | |   \\/   | |   _  \\  |   ____||   _  \\        |           | /  __  \\   /  __  \\  |  |        /       |\033[0m     by LordOfTheIoT")
		print("                \033[1;34m|  |_)  | |  |__|  | |  |  |  | |   \\|  | |  |__      |   \\|  | |  |  |  | |  \\  /  | |  |_)  | |  |__   |  |_)  |       `---|  |----`|  |  |  | |  |  |  | |  |       |   (----`\033[0m      https://github.com/Lord-of-the-IoT")
		print("                \033[1;34m|   ___/  |   __   | |  |  |  | |  . `  | |   __|     |  . `  | |  |  |  | |  |\\/|  | |   _  <  |   __|  |      /            |  |     |  |  |  | |  |  |  | |  |        \\   \\\033[0m")
		print("                \033[1;34m|  |      |  |  |  | |  `--'  | |  |\\   | |  |____    |  |\\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\\  \\----.       |  |     |  `--'  | |  `--'  | |  `----.----)   |\033[0m")
		print("                \033[1;34m| _|      |__|  |__|  \\______/  |__| \\__| |_______|   |__| \\__|  \\______/  |__|  |__| |______/  |_______|| _| `._____|       |__|      \\______/   \\______/  |_______|_______/\033[0m")

		print('\n\n    a tool to interact with phone identifiers, such as ICCIDs and phone numbers')

	def gen_iccid(self):
		mii = '89' #major industry identifier
		cc = '' #country code
		iin = '' # issuer identifier number
		iain = '' #individual account identification number
		c = '' #luhn check number

		i = 1
		print('\n\n        select country code (some are not counties)')
		for country, code in self.country_code.items():
			print(f'            [{i:03}]  {country:45}     (country code is {code})')
			i+=1
		choice = input('        choose the country code>').strip()
		if choice.isnumeric()==False:
			self.error('not a valid choice')
			return

		country = list(self.country_code.keys())[int(choice)]
		cc = self.country_code[country]

		self.banner()
		print(f'\n\n        code so far: {mii}{cc}')
		print(f'        country: {country}')

		sleep(10)



	def gen_imsi(self):
		self.error('sry :( not programmed yet')
	def gen_imei(self):
		self.error('sry :( not programmed yet')
	def decode_iccid(self):
		self.error('sry :( not programmed yet')
	def decode_imsi(self):
		self.error('sry :( not programmed yet')
	def decode_imei(self):
		self.error('sry :( not programmed yet')

	def cli(self):
		while True:
			self.banner()

			print('\n\n        options')
			print('            [1] generate ICCID')
			print('            [2] generate IMSI')
			print('            [3] generate IMEI')
			print('            [4] decode ICCID')
			print('            [5] decode IMSI')
			print('            [6] decode IMEI')
			choice = input('\033[0m       enter choice>').strip()

			match choice:
				case '1':
					self.gen_iccid()
				case '2':
					self.gen_imsi()
				case '3':
					self.gen_imei()
				case '4':
					self.decode_iccid()
				case '5':
					self.decode_imsi()
				case '6':
					self.decode_imei()
				case _:
					self.error('not a valid choice')



if __name__ == '__main__':
	tool = Tool()
	tool.cli()
