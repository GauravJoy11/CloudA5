from flask import Flask

app=Flask(__main__)

@approute('/t')
def home:
  return "<h1>This is my fist python app for web application</h1>"
  
if __name__='__main__'
 app.run(host="0.0.0.0', port=8080)


