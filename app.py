#Routes & Url Kullanımı:
from flask import Flask, request

app = Flask(__name__)

@app.route( '/hello', methods=['GET', 'POST']) #Methodları tanıtıyoruz.
def hello():
    return "hello world"
#Post methodunu kullanmak için cmd'e curl -X POST "url"yi yazmalısın.
#Get methodu için curl "url" yazman yeterli.


#Route ile girilen url'yi çalıştırmak için aşağıdaki gibi yapılır.
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
#integer olduğunu belirtmeden bu kodu yazarsanız "10+20=1020" gibi bir çıktı alırsınız.
def add(number1,number2):
    return f'{number1} + {number2} = {number1 + number2}'

#Parametre girişi:
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.key():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting},{name}'
# Url kısmına /handle_url_params?name-mike&greeting-hello yazarsanız alacağınız çıktı şu olur:
# "ImmutableMulltiDict([('name','Mike'),('greeting','Hello')])
    else:
        #Parametreler eksik mi diye kontrol edip hata mesajı verir.
        return 'Bazı parametreler eksik.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5555, debug=True)
    #Port'u 5555 olarak ayarladık.