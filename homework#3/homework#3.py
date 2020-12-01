from flask import Flask, render_template


app = Flask(__name__)



@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


@app.route('/terms', methods =['GET'])
def Terms_of_use():
    return render_template('terms_of_use.html')

@app.route('/privacy', methods =['GET'])
def privacy():
    return render_template('privacy.html')    

@app.route('/football', methods =['GET'])
def football():
    return render_template('football.html')

@app.route('/about', methods =['GET'])
def about():
    return render_template('about.html')



if __name__=='__main__':
    app.run(port = 7000, debug = True) 

