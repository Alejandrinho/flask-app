from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/convert', methods = ['POST'])
def convert_json():
    data = request.data
    output_text = data.decode('utf-8')
    response_raw = 'raw'
    response = app.response_class(
        response_raw,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/hello', methods = ['GET'])
def hello():
    return 'Hello'

@app.route('/', methods = ['GET'])
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')