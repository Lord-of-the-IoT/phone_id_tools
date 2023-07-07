import os
import random
from time import sleep

#{country: [ccn, {issuer: [mnc, mcc, iain_length]} ] }
data = {'Abkhazia': ['7',
                     {'A-Mobile':     ['68', '289'],
                      'A-Mobile':     ['88', '289'],
                      'Aquafon':     ['67', '289']}
                    ],
        
        'United Kingdom': ['44',
                           {'Teleware':     ['19', '234'],
                            'Vodafone':     ['07', '234'],
                            'NCSC':     ['56', '234']}
                          ],

        'China': ['86',
                  {'China Telecom': ['12', '460'],
                   'China Unicom': ['10', '460'],
                   'China Mobile': ['07', '460']}
                 ],

        'United States': ['1',
                          {'AT&T Mobility': ['410', '313'],
                           'Northstar Technology': ['299', '316'],
                           'verizon Wireless': ['277', '312']}
                         ]
       }

class LuhnAlgorithm:
  def gen(self, digits):
    if digits.isnumeric():
      digits=[digit for digit in digits.strip()]
      for i in range(len(digits)-1, 0, -2):
        odd = int(digits[i])*2
        if odd>9:
          odd = (odd % 10) + (odd // 10)
        digits[i]=str(odd)
      luhn_value= sum([int(digit) for digit in digits])%10
      luhn_checksum = (9*luhn_value)%10
      return str(luhn_checksum)
          
  def check(self, digits):
    if digits.isnumeric():
      digits=[digit for digit in digits.strip()]
      for i in range(len(digits)-2, 0, -2):
        odd = int(digits[i])*2
        if odd>9:
          odd = sum([int(digit) for digit in str(odd)])
        digits[i]=str(odd)
    luhn_value=sum([int(digit) for digit in digits])%10
    return luhn_value==0



class ICCID:
  """
  Intergrated Circuit Card IDentifier  (18-22 digits)
  MII + CCN + IIN + IAIN + C
  
  issuer identification        individual account ID      luhn check
  number <=7               number <=14 >=11           number
  |****************|     |****************************|      |*|
  MM(C-CCC)(I-IIIII)     (NNNNNNNNNNN-NNNNNNNNNNNNNN)        C
  
  
  MM- (mii) major industry identifier. always 89 for telecommunications
  CC- (ccn) 1-3 digits   country code assigned by International Telephone Union- Not mobile country codes used in IMSI
  II- (iin) Issuer identifier- also called mnc
  N - (iain) individual account identification number
  C - (lcn) luhn check sum
  """
  def __init__(self, cli):
    self.cli= cli

  def gen(self):
    mii = '89' #major industry identifier
    country = '' #country from the data variable including country code and individual identifier number
    iain = '' #individual account identification number
    lcn = '' #luhn check number
    iccid = mii #the ICCID
    
    self.cli.banner(f'\n\n         country: {country}\n         network operator:')
    print('\n\n        select country (some are not counties)')
    choice = self.cli.select(data.keys(), input_string='choose the country code')
    country = data[list(data.keys())[choice]]
    country.append(list(data.keys())[choice])
    
    self.cli.banner(f'\n\n         country: {country[2]}\n         network operator:')
    print('\n\n        select network operator')
    choice = self.cli.select(country[1].keys(), input_string='choose the network operator')
    operator = list(country[1].keys())[choice]
    iccid += country[1][operator][1]+country[1][operator][0]
    self.cli.banner(f'\n\n        ICCID so far: {mii}{country[1][operator][1]}{country[1][operator][0]}\n         country: {country[2]}\n         network operator: {operator}')
    print('\n\n        select length of Individual Account Idenification Number:')
    choice = self.cli.select(range(11, 22-len(iccid)), input_string='choose the length')+11
    
    iain = ''.join([str(random.randint(0, 9)) for _ in range(choice)])
    iccid += iain
    self.cli.banner(f'\n\n        ICCID so far: {iccid}\n        country: {country[2]}\n        network operator: {operator}')
    
    lcn = self.cli.luhn.gen(iccid)
    iccid+=lcn
    self.cli.banner(f'\n\n        ICCID Calculated!\n        ICCID: {iccid}\n         country: {country[2]}\n         network operator: {operator}')
    if self.cli.luhn.check(iccid):
      print('        valid luhn checksum!')
    else:
      self.cli.error('invalid luhn checksum!')
    input()
    
  def decode(self):
    country = ''
    operator = ''
    mcc = ''
    mnc = ''
    print('\n\n        enter ICCID to decode')
    iccid = input('          >').strip()
    if self.cli.luhn.check(iccid)==False:
      self.cli.error('invalid ICCID! not a valid luhn checksum')
      return -1
    if len(iccid)>22:
      self.cli.error('invalid ICCID! to long')
      return -1
    if len(iccid)<18:
      self.cli.error('invalid ICCID! too short')
      return -1
    if iccid[0:2]!='89':
      self.cli.error('invalid ICCID! not telecoms mii')
      return -1
    stripped_iccid = iccid[2:-1] #strip mii and luhn checksum
    for i in range(3, 0, -1): #loop through all possible lengths of mcc
      mcc = stripped_iccid[:i]
      for country_key in data.keys():
        for operator_data in data[country_key][1].values():
          if operator_data[1]==mcc:
            country = country_key
            stripped_iccid = stripped_iccid[len(mcc)-1:]
            break
    if country!='':
      for i in range(3, 2, -1):
        mnc = stripped_iccid[:i]
        for operator_key in data[country][1].keys():
          if data[country][1][operator_key]==mnc:
            operator = operator_key
            stripped_iccid = stripped_iccid[len(mnc)-1:]
            break
      self.cli.banner(f'\n\n        ICCID: {iccid}\n         country: {country[2]}\n         network operator: {operator}')
      input()
    


class CLI:
  def __init__(self):
    self.luhn = LuhnAlgorithm()
    self.iccid = ICCID(self)
    
  def error(self, reason):
    print('\n\n        \033[1;31m[!] '+reason+'\033[0m')
    sleep(3)
    
  def banner(self, banner_string=''):
    os.system('clear')
    print("                \033[1;34m.______    __    __    ______   .__   __.  _______    .__   __.  __    __  .___  ___. .______    _______ .______         .___________.  ______     ______    __          _______.\033[0m")
    print("                \033[1;34m|   _  \\  |  |  |  |  /  __  \\  |  \\ |  | |   ____|   |  \\ |  | |  |  |  | |   \\/   | |   _  \\  |   ____||   _  \\        |           | /  __  \\   /  __  \\  |  |        /       |\033[0m     by LordOfTheIoT")
    print("                \033[1;34m|  |_)  | |  |__|  | |  |  |  | |   \\|  | |  |__      |   \\|  | |  |  |  | |  \\  /  | |  |_)  | |  |__   |  |_)  |       `---|  |----`|  |  |  | |  |  |  | |  |       |   (----`\033[0m      https://github.com/Lord-of-the-IoT")
    print("                \033[1;34m|   ___/  |   __   | |  |  |  | |  . `  | |   __|     |  . `  | |  |  |  | |  |\\/|  | |   _  <  |   __|  |      /            |  |     |  |  |  | |  |  |  | |  |        \\   \\\033[0m")
    print("                \033[1;34m|  |      |  |  |  | |  `--'  | |  |\\   | |  |____    |  |\\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\\  \\----.       |  |     |  `--'  | |  `--'  | |  `----.----)   |\033[0m")
    print("                \033[1;34m| _|      |__|  |__|  \\______/  |__| \\__| |_______|   |__| \\__|  \\______/  |__|  |__| |______/  |_______|| _| `._____|       |__|      \\______/   \\______/  |_______|_______/\033[0m")
    
    print('\n\n    a tool to interact with phone identifiers, such as ICCIDs and phone numbers')
    print(banner_string)
    
  def __call__(self):
    while True:
      self.banner()
      
      print('\n\n        options')
      print('            [1] generate ICCID')
      print('            [2] generate IMSI')
      print('            [3] generate IMEI')
      print('            [4] decode ICCID')
      print('            [5] decode IMSI')
      print('            [6] decode IMEI')
      choice = input('\033[0m       enter choice>').strip()
      
      match choice:
        case '1':
          self.iccid.gen()
        case '2':
          self.error("not programmed yet :(")
        case '3':
          self.error("not programmed yet :(")
        case '4':
          self.iccid.decode()
        case '5':
          self.error("not programmed yet :(")
        case '6':
          self.error("not programmed yet :(")
        case _:
          self.error('not a valid choice')
    
    
  def select(self, options, input_string='', banner_string=''):
    while True:
      print('        options')
      i=1
      for option in options:
        print(f'            [{i}] {option}')
        i+=1
      if input_string:
        choice = input(f'\033[0m       {input_string}>').strip()
      else:
        choice = input('\033[0m       eneter choice>').strip()
      if choice.isnumeric():
        return int(choice)-1
      self.error('invalid choice!')
      self.banner(banner_string)

if __name__ == '__main__':
  cli = CLI()
  cli()
