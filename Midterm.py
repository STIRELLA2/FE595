from flask import Flask
from flask_restful import Resource, Api, regparse

app = Flask(__name__) # "__main__"
api = Api(app)

@app.route('/Midterm', methods=['GET', 'POST'])
def flask_import():
  return """<html>


 
<body>
<h1>FA595 Midterm<h1><br><br>
<h2>Group 8: Zemin Li, Sherri Putnam, Spencer Tirella</h2>
<b>
<p>Deliverables:<br>
1. Created a flask end point accessible to the entire internet hosted on an AWS machine<br>
2. Able to accept cURL calls on one route and successfully return a 200 status when called<br>
3. Able to accept in a request with a payload including a string and a requested NLP service<br>
&nbsp;&nbsp&nbsp;&nbsp;Our project is capable of returning 2 services for each member of our group<br>
</p>
</body>
</html>
  """

def post(string):
    parser = reqparse.Requestparser()
    parser.add_argument('string', required = TRUE, type = str)
    args = parser.parse_args()
    return{'NLP Service':args['string']}, 200

#Service 1 
#Service 2 
#Service 3
#Service 4
#Service 5
#Service 6

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080
