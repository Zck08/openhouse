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

@app.route('/verificacion')
def verificacion():
    return render_template('verificacion.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/junta')
def junta():
    return render_template('junta.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/plan')
def plan():
    return render_template('plan.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')  # asegúrate que este archivo esté en la carpeta /templates

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')  # asegúrate que este archivo esté en la carpeta /templates


@app.route('/enviar', methods=['POST'])
def enviar():
    correo = request.form['ced']
    contrasena = request.form['pass']

    asunto = "Confirmación de registro"
    mensaje = f"""

        Bienvenido/a a CTP Calle Blancos
        Gracias por registrarte. Estamos encantados de tenerte con nosotros.
    
        Estos son tus datos de acceso:
        Correo electrónico: {correo}
        Contraseña: {contrasena}
    
        Para activar tu cuenta y confirmar tu registro, haz clic en el siguiente botón:
    
        https://www.ctpcalleblancos.site/confirmacion
    
        Si no realizaste este registro, puedes ignorar este mensaje.
    
        Saludos cordiales,
        Equipo de CTP Calle Blancos
    """

    msg = Message(asunto,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[correo])
    msg.body = mensaje
    msg.charset = 'utf-8'  # solución para caracteres como la ñ

    try:
        mail.send(msg)
        flash('Correo enviado correctamente.')
        return redirect('/verificacion')
    except Exception as e:
        flash(f'Error al enviar correo: {e}')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
