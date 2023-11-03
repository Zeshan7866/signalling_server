print("hello world")


from flask import Flask, request, Response
import json


app = Flask(__name__)


data = {}


@app.route('/test')
def test():
    return Response('{"status":"ok"}', status=200, mimetype='application/json')


@app.route('/offer', methods=['POST'])
def offer():
    if request.form["type"] == "offer":
        data["offer"] = {"id" : request.form['id'], "type" : request.form['type'], "sdp" : request.form['sdp']}
        return Response(status=200)
    else:
        return Response(status=400)

@app.route('/answer', methods=['POST'])
def answer():
    if request.form["type"] == "answer":
        data["answer"] = {"id" : request.form['id'], "type" : request.form['type'], "sdp" : request.form['sdp']}
        return Response(status=200)
    else:
        return Response(status=400)

@app.route('/get_offer', methods=['GET'])
def get_offer():
    if "offer" in data:
        j = json.dumps(data["offer"])
        del data["offer"]
        return Response(j, status=200, mimetype='application/json')
    else:
        return Response(status=503)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    if "answer" in data:
        j = json.dumps(data["answer"])
        del data["answer"]
        return Response(j, status=200, mimetype='application/json')
    else:
        return Response(status=503)
    
@app.route('/ice-offerer', methods=['POST'])
def ice_offerer():
    if request.form["type"] == "candidate":
        data["ice-offerer"] = data.get("ice-offerer", []) + [request.form['candidate']]
        return Response(status=200)
    else:
        return Response(status=400)

@app.route('/ice-answerer', methods=['POST'])
def ice_answerer():
    if request.form["type"] == "candidate":
        data["ice-answerer"] = data.get("ice-answerer", []) + [request.form['candidate']]
        return Response(status=200)
    else:
        return Response(status=400)

@app.route('/get-ice-offerer', methods=['GET'])
def get_ice_offerer():
    if "ice-offerer" in data:
        j = json.dumps(data["ice-offerer"])
        data["ice-offerer"] = []
        return Response(j, status=200, mimetype='application/json')
    else:
        return Response(status=503)

@app.route('/get-ice-answerer', methods=['GET'])
def get_ice_answerer():
    if "ice-answerer" in data:
        j = json.dumps(data["ice-answerer"])
        data["ice-answerer"] = []
        return Response(j, status=200, mimetype='application/json')
    else:
        return Response(status=503)






if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

