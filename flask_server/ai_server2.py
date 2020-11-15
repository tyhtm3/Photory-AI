from flask import Flask, request, render_template
from flask_cors import CORS
from TextGeneration.Module import StoryGenerator_photory as SGEN

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def index_page():
    return "AI server2!"

@app.route('/tale')
def tale():
    st = SGEN.StoryGeneration()
    return st.Generate_p_sampling('나는 서있다')

if __name__=='__main__':
    app.run(host='0.0.0.0')