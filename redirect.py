from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/page')
def index():
    return redirect('http://150.158.55.168:5555')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
