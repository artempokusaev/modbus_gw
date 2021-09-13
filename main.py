from flask import Flask
from flask import request
from pymodbus.client.sync import ModbusTcpClient

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'>Azimutprint</h1>"

@app.route("/get_readings")
def get_readings():
    client = ModbusTcpClient('192.168.1.200')
    client.connect()

    regaddr = request.args.get('devaddr')  # Address to read
    regcount = 1  # kol-vo registrov
    mba = 127  # nomer ustroystva modbus

    result = client.read_input_registers(address=regaddr, count=regcount, unit=mba)
    readings = result.registers

    client.close()
    r= str(readings[0])
    return r

@app.route("/reset")
def reset():
    client = ModbusTcpClient('192.168.1.200')
    client.connect()

    regaddr = 1  # Address to write
    mba = 127  # nomer ustroystva modbus
    data = 1  # data to write

    client.write_register(address=regaddr, value=data, unit=mba)
    client.close()
    return "Counter reseted"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
