from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap4
import math

# Inicializando o Flask e o Bootstrap-Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UMACHAVEDETESTE'
Bootstrap4(app)

# Renderizando o form que irá fazer o request para a API com o WTFlask

class Form(FlaskForm):
    cateto_a = FloatField('Cateto A', validators=[DataRequired(message='Você precisa inserir um numero válido!')])
    cateto_b = FloatField('Cateto B', validators=[DataRequired(message='Você precisa inserir um numero válido!')])
    submit = SubmitField('Submit')

# Criando a rota para a renderizar o HTML
@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()

    # Validando o formulario e pegando os itens para retornar o calculo do teorema
    if form.validate_on_submit():
        cat_a = form.cateto_a.data
        cat_b = form.cateto_b.data
        return redirect(url_for('result', cat_a=cat_a, cat_b=cat_b))

    return render_template('index.html', form=form)

@app.route('/result')
def result():
    # Usando o modulo request.args para pegar as informações enviadas pelo formulario
    cat_a = float(request.args.get('cat_a'))
    cat_b = float(request.args.get('cat_b'))

    # Usando o métoddo math.pow do modulo math do Python para receber o valor da Hipotenusa e o math.sqrt para achar a raiz quadrada
    # Além do método round para limitar as casas arredondadas para 2 casas após a virgula

    hipotenusa_ao_quadrado = math.pow(cat_a, 2) + math.pow(cat_b, 2)
    hipotenusa = round(math.sqrt(hipotenusa_ao_quadrado), 2)

    # Criando um dicionario para ser transformado em JSON com os resultados
    result = {
        'result': {
            'Cateto A': cat_a,
            'Cateto B': cat_b,
            'Hipotenusa': hipotenusa
        }
    }

    # Retornando um JSON com o metodo Jsonify do Flask com os valores dos catetos e da Hipotenusa
    return jsonify(result)

# Inicializando o Flask

if __name__ == "__main__":
    app.run(debug=True)
