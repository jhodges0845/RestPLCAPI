from waitress import serve
from flask import Flask, jsonify, request
from plc_interface.interface import write_plc, read_plc

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if(request.method == "GET"):
        data = "Hello World"
        return jsonify({'data': data})

@app.route("/plc/write/<ip_address>/<tag_name>/<data_type>/<value>", methods = ["GET"])
def plc_write(ip_address, tag_name, data_type, value):

    print("REST-API interface initiated")
    write_plc(ip_address, tag_name, data_type, value)
    return "request completed"

@app.route("/plc/read/<ip_address>/<tag_name>", methods = ["GET", "POST"])
def plc_read(ip_address, tag_name):
    print("REST-API interface initiated")
    data = read_plc(ip_address, tag_name)
    return jsonify({'data': data})
    

if __name__ == "__main__":
    #app.run(debug = True, host="0.0.0.0", port=5000)
    serve(app, host="0.0.0.0", port=5000)