import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s

mynums = raw_input('PLease enter ten numbers with comma in between them(,):')
mynums = [int(x) for x in mynums.split(',')]

max=-1444
for i in range(30):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    sum = 0
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(mynums,tmp)) 

    for i in r:
	if i>=4:
		sum+=1
    if sum>max:
	max=sum
	name=date_str


print 10*"-"
print "The most profitble day would be ",name," with ",max,"victories"
