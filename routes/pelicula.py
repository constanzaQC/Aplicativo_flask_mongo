from app import app
from flask import Flask, request, render_template, session
from models.pelicula import Pelicula
from models.genero import Genero
from bson.objectid import ObjectId

@app.route("/pelicula/",methods=["GET"])
def listarPelicula():
    try:
        mensaje=None
        peliculas=Pelicula.objects()
    
    except Exception as error:
        mensaje=str(error)

    return {"mensaje": mensaje,"peliculas": peliculas}

@app.route("/pelicula/", methods=['POST'])
def addPelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=Genero.objects(id=datos['genero']).first()
            if genero is None:
                mensaje="genero no existe, no se puede crear la pelicula"            
           
            else:
                datos['genero']=genero
                pelicula= Pelicula(**datos)
                pelicula.save()
                estado=True
                mensaje="Pelicula agregado correctamente"
        else:
            mensaje="no permitido"
        
    except Exception as error:
        mensaje=str(error)
        
    return{"estado":estado, "mensaje":mensaje}


@app.route("/pelicula/", methods=['PUT'])
def updatePelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='PUT':
            datos=request.get_json(force=True)
            #obtener pelicula por id 
            pelicula=Pelicula.objects(id=datos['id']).first()
            #actualizar sus atributos
            pelicula.codigo= datos['codigo']
            pelicula.titulo= datos['titulo']
            pelicula.protagonista= datos['protagonista']
            pelicula.resumen= datos['resumen']
            pelicula.foto= datos['foto']
            genero=Genero.objects(id=datos['genero']).first()
            if genero is None:
                mensaje="no se actualiza el genero."
            else:
                pelicula.genero=genero
            pelicula.save()
            mensaje =f"{mensaje} pelicula actualizada" 
            estado=True
        else: 
            mensaje="no permitido"
    except Exception as error:
        mensaje=str(error)
        
    return{"estado":estado, "mensaje":mensaje}

@app.route("/pelicula/", methods=['DELETE'])
def deletePelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='DELETE':
            datos=request.get_json(force=True)
            pelicula = Pelicula.objects(id=datos['id']).first()
            if pelicula is None:
                mensaje="no se puede eliminar la pelicula"
            else:
                pelicula.delete()
                estado=True
                mensaje="pelicula eliminada satisfactoriamente"
        else:   
            mensaje="no permitido"
    except Exception as error:
        mensaje=str(error)
    
    return {"estado": estado, "mensaje":mensaje}
@app.route("/peliculas/",methods=["GET"])
def listarPeliculas():
    if ("user" in session):
        peliculas= Pelicula.objects()
        generos=Genero.objects()
        return render_template("listarPelicula.html",
                           peliculas=peliculas,generos=generos)
    else:
        mensaje="debe ingresar primero"
        return render_template("iniciarSesion.html", mensaje=mensaje)
@app.route("/agregarPelicula/",methods=["GET"])
def AgregarPelicula():
    generos=Genero.objects()
    return render_template("AgregarPelicula.html", generos=generos)

@app.route("/editarPelicula/<string:id>/",methods=["GET"])
def EditarPelicula(id):
    peliculas=Pelicula.objects(id=ObjectId(id)).first()
    generos=Genero.objects()
    
    return render_template("EditarPelicula.html", peliculas=peliculas, generos=generos)


