from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def index_page():
    return "AI server2!"

if __name__=='__main__':
    app.run(host='0.0.0.0')