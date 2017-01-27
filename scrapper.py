from  BeautifulSoup import BeautifulSoup
import urllib
import sys
from dateutil import relativedelta as rt
import datetime

page = open("git.html","r")

soup = BeautifulSoup(page)

options = {
            'secs': 'seconds',
            'mins': 'minutes',
            'hours': 'hours',
            'days': 'days', 
            'weeks': 'weeks',
            'months': 'months',
            'years': 'years'
}

table = soup.find("table", { "class": "repositories" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    count = 0
    repo_name=""
    repo_Age=""
    for cell in cells:
        if count == 0:
            repo_name=cell.text
        if count == 4:
            number = cell.text.split()[0]
            unit = options[cell.text.split()[1]]
            arr=[(unit,number)]
  
            time_dict = dict((unit,int(number)) for unit,number in arr)

            dt = rt.relativedelta(**time_dict)
            updated_time=datetime.datetime.now() - dt

            check_time=datetime.datetime.now() - rt.relativedelta(days=30)
           
            if check_time > updated_time:
              print "Repository: {} Last_updated: {}".format(repo_name,updated_time)
            
        count = count+1 
