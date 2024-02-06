


from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "JHON023"

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():


    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'teste' and senha == '123':
        return render_template("usuarios.html")
    else:

        return redirect('/')

if __name__ in "__main__":
    app.run(debug=True)