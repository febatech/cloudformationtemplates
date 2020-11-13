import json,requests,boto3

def run(link):
    url = link
# Getting the image from internet
    r = requests.get(url)
    f_name=url.split('/')[-1]
    with open(f_name, 'wb') as f:
        f.write(r.content)

# uploading the image to S3
    s3=boto3.resource('s3')
    data=open(f_name, 'rb')
    s3.Bucket('kali-linus').put_object(Key=f_name, Body=data)





with open("Links.json") as f:
    data=json.load(f)

for link in data['Images']:
    run(link['Link'])
