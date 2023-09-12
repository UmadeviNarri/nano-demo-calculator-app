from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return 'Hello world!', 200

@app.route('/calculator/add', methods=['POST'])
def add():
    try:
        data = request.json
        first = data.get('first', 0)
        second = data.get('second', 0)
        result = first + second
        return jsonify({"result": result}), 200
    except Exception as e:
        return str(e), 400

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    try:
        data = request.json
        first = data.get('first', 0)
        second = data.get('second', 0)
        result = first - second
        return jsonify({"result": result}), 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
