import angus
from pprint import pprint
import csv
import urllib
import pandas
df = pandas.read_csv('img-url-list.csv')
values = df['photo'].values
url=''
conn = angus.connect()
service = conn.services.get_service('age_and_gender_estimation', version=1)
f1 = open('predict_age_gender.csv', 'wt')
writer = csv.writer(f1)
writer.writerow(('photo', 'age', 'gender'))
for value in values:
    try:
        f = open('00000001.jpg','wb')
        f.write(urllib.urlopen(value).read())
        f.close()

        job = service.process({'image': open('./00000001.jpg', 'rb')})
       # pprint(job.result)
        res=job.result

        for face in res['faces']:
         writer.writerow((value, face['age'], face['gender']))
         print(value, face['age'],face['gender'],face['age_confidence'],face['gender_confidence'])

    except:
        print "Invalid Url:"+str(value)
