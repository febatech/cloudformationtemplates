import requests,boto3,csv



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
    s3.Bucket('myimportbucket').put_object(Key=f_name, Body=data)


with open('Links.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for x in csv_reader:
        run(x[0])





