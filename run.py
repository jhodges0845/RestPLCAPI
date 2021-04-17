from flask import Flask, jsonify, request
from plc_interface.interface import write_plc

app = Flask(__name__)

@app.route("/", methods = ["GET", "SET"])
def home():
    if(request.method == "GET"):
        data = "Hello World"
        return jsonify({'data': data})

@app.route("/plc/write/<ip_address>/<tag_name>/<data_type>/<value>")
def plc_write(ip_address, tag_name, data_type, value):
    print("REST-API interface initiated")
    write_plc(ip_address, tag_name, data_type, value)
    return "request completed"

if __name__ == "__main__":
    app.run(debug = True)