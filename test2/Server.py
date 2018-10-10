from flask import Flask,jsonify,request

app = Flask(__name__)
# WS de respuesta en directorio raiz.

'''akkakakaakakkakakak
kakakaakakakakkakakaka
hahahahakikakakakakaka'''

dic ={'1' : 'Paco', '2' : 'Pepe'}
@app.route('/users/<id>',methods=['GET'])
def get_user(id):
    user = dic[id]
    return jsonify(user)

@app.route('/concat/',methods=['GET'])
def concat():
    cad1 = request.args.get('cad1')
    cad2 = request.args.get('cad2')
    result = cad1 + cad2
    return jsonify(result)

@app.route('/calculate/<num>',methods=['GET'])
def calcular_sqr(num):
    num = int(num)
    num = num * num
    return jsonify(num)

@app.route('/calculate/',methods=['GET'])
def calcular_param():
    num = request.args.get('num')
    num = int(num)
    result = num * num
    return jsonify(result)

@app.route('/sayhello',methods=['GET'])
def saludar():
    var = 'hello'
    return jsonify(var)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'URJC University' : 'API Testing'})

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)