from app import app,db,recaptcha
from flask import Flask, request, render_template, session
from models.usuario import Usuario
import yagmail
import threading
from dotenv import load_dotenv
import os
import random, string

load_dotenv()


@app.route("/")
def login():
    return render_template("iniciarSesion.html")

@app.route("/usuario/",methods=["GET"])
def listarUsuario():
    try:
        mensaje=None
        usuarios=Usuario.objects()
    except Exception as error:
        mensaje=str(error)
    return {"mensaje": mensaje,"usuarios": usuarios}

@app.route("/home/")
def home():
    return render_template("contenido.html")

@app.route("/iniciarSesion/",methods=["POST"])
def iniciarSesion():
    mensaje=" "
    try:
        if request.method=='POST':
            if recaptcha.verify():
                print("SUCCESS")
            else:
                print("FAILED")
            username = request.form['txtUser']
            password = request.form['txtPassword']
            print(username)
            print(password)

            usuario=Usuario.objects(usuario=username,password=password).first()
            print(usuario)
            ula=usuario.password
            hola=usuario.usuario
            print(ula)
            print(hola)
            
            correo=os.environ.get("CORREO")
            clave=os.environ.get("ENVIAR_CORREO")
            if usuario:
                session['user']=username
                session['user_name']=f"{usuario.nombres} {usuario.apellidos}"
                email= yagmail.SMTP(correo,clave, encoding="utf-8")
                asunto="Ingreso al sistema"
                mensaje=f"ha ingresado al aplicativo {usuario.nombres} {usuario.apellidos}"
                thread=threading.Thread(target=enviarCorreo, args=(email, [usuario.correo], asunto,mensaje))
                thread.start()
                return render_template("contenido.html")
            else:
                mensaje="credenciales incorrectas"
    except Exception as error:
        mensaje=str(error)

    return render_template("iniciarSesion.html", mensaje=mensaje)
def enviarCorreo(email=None, destinatario=None, asunto=None, mensaje=None):
   email.send(to=destinatario, subject=asunto, contents=mensaje)
    
@app.route("/cerrarSesion/")
def cerrarSesion():
    session.clear()
    mensaje="sesion cerrada"
    return render_template("iniciarSesion.html", mensaje=mensaje)

def generar_contraseña(n=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(n))

@app.route("/newcontrasena/", methods=["GET","POST"])
def recuperar():
    mensaje = ""
    try:
        if request.method == 'POST':
            usuario = request.form['txtusuario']
            correo_form = request.form['txtcorreo']

            # Verifica que el usuario exista
            user = Usuario.objects(usuario=usuario, correo=correo_form).first()
            if user:
                nueva_pass = generar_contraseña()
                user.password = nueva_pass  
                user.save()

                correo_envio = os.environ.get("CORREO")
                clave_envio = os.environ.get("ENVIAR_CORREO")
                email = yagmail.SMTP(correo_envio, clave_envio)
                asunto = "Recuperación de contraseña"
                mensaje = f"Hola {user.nombres}, tu nueva contraseña es: {nueva_pass}"

                email.send(to=user.correo, subject=asunto, contents=mensaje)
                return render_template("iniciarSesion.html", mensaje="Nueva contraseña enviada al correo")
            else:
                mensaje = "Usuario o correo incorrecto"
    except Exception as e:
        mensaje = str(e)

    return render_template("recuperarContraseña.html", mensaje=mensaje)