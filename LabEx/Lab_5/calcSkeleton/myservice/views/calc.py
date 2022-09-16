from flakon import JsonBlueprint
from flask import Flask, request, jsonify
from calculator import calculator as c


calc = JsonBlueprint('calc',__name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.sum(m,n)

    return jsonify({'result':str(result)})

@calc.route('/calc/divide', methods=['GET'])
def divide():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.divide(m,n)

    return jsonify({'result':str(result)})

@calc.route('/calc/sub', methods=['GET'])
def subtract():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.subtract(m,n)

    return jsonify({'result':str(result)})

@calc.route('/calc/multiply', methods=['GET'])
def multiply():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = c.multiply(m,n)

    return jsonify({'result':str(result)})
