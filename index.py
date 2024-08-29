from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/ayuda')
def ayuda():
    return render_template('Ayuda.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        flash(f'Gracias por tu mensaje, {nombre}. Nos pondremos en contacto contigo en breve.')
        
        return render_template('agradecimiento.html', nombre=nombre, email=email, mensaje=mensaje)
    
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
