from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello world!'

@app.route('/contactus')
def contact_page():
    return '911'

@app.route('/careers')
def careers_page():
    return 'seeking employees'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
