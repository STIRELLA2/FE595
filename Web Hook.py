from flask import Flask
app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hellow_world():
    return "Hellow world."

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
