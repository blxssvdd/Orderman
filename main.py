from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = [
        {'name': 'Маргарита', 'ingredients': 'Томати, Моцарела, Базилік', 'price': '8.99$'},
        {'name': 'Пепероні', 'ingredients': 'Томати, Моцарела, Пепероні', 'price': '9.99$'},
        {'name': 'Гавайська', 'ingredients': 'Томати, Моцарела, Курка, Ананас', 'price': '10.99$'}
    ]
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
