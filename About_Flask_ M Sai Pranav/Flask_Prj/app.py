from flask import Flask, render_template, request, redirect
import os, boto3
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    banks = ['sbi', 'kotak', 'citi', 'amex', 'bob', 'axis', 'hdfc', 'idbi', 'yesbank', 'indusind']
    return render_template('feba.html', banks=banks)


@app.route('/dropdown', methods = ['POST'])
def dropp():
    dropdownval = request.form.get('bank')
    print(dropdownval)
    file = "python "+dropdownval+".py"
    os.system(file)
    # s3 = boto3.resource('s3')
    # data = open(dropdownval+".json", 'rb')
    # s3.Bucket('kardfinder-banks-json-files-repo').put_object(Key=dropdownval+".json", Body=data)
    # object_acl = s3.ObjectAcl('kardfinder-banks-json-files-repo', dropdownval+".json")
    # object_acl.put(ACL='public-read')

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run()
