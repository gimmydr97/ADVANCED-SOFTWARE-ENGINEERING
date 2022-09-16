from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calc = JsonBlueprint('calc', __name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
    #http://127.0.0.1:5000/calc/sum?m=3&n=5
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m

    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1

    return jsonify({'result':str(result)})

@calc.route('/calc/sub', methods=['GET'])
def subtract():
    #http://127.0.0.1:5000/calc/sub?m=3&n=5
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = m

    if n < 0:
        for i in range(abs(n)):
            result += 1
    else:
        for i in range(n):
            result -= 1
            
    return jsonify({'result':str(result)})

@calc.route('/calc/mul', methods=['GET'])
def multiply():
    #http://127.0.0.1:5000/calc/mul?m=3&n=5
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result =0
    
    if n != 0 or m !=0 :
        negativeResult = m > 0 and n < 0 or m < 0 and n > 0
        n = abs(n)
        m = abs(m)
        
        while ( n > 0):
            result += m
            n -= 1
            
        result = -result if negativeResult else result

    return jsonify({'result':str(result)})

@calc.route('/calc/div', methods=['GET'])
def divide():
    #http://127.0.0.1:5000/calc/div?m=6&n=2
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))

    result = 0

    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)

    if n == 0:
        raise ZeroDivisionError('You cannot divide by 0!')

    while (m - n >= 0):
        m -= n
        result += 1
    
    result = -result if negativeResult else result

    return jsonify({'result':str(result)})
