from behave import *
import requests
import re
UB = [2.0,5.0]
UK = [5.0,10.0]
RL = [7,14]
URL = "http://dingdata.nl/batterij"
for i in UB:
   for j in UK:
      for k in RL:
         print('antwoord : ',(i - j) / (j / k), ' UB: ', i, ' UK: ', j, ' RL: ', k)
         '''r = requests.get(url = URL, params = {'I': i, 'UK': j})
         response = r.json()
         a = response['resultaten']['antwoord']
         print('antwoord: ',response)
         print('alles: ',a)
         b = re.search('\w*? = ([\d.]*) \w*',a).group(1)
         print('regexed ant: ',b)'''