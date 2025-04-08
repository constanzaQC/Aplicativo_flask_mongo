/**
 * Función que se encarga de hacer
 * una petición al backend para
 * agregar un género.
 */

function agregarGenero() {
    const genero = {
        nombre: document.getElementById('txtGenero').value
    }
    const url = "/genero/"

    fetch(url, {
        method: "POST",
        body: JSON.stringify(genero),
        headers: {
            "Content-Type": "application/json",
        }
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        if (resultado.estado) {
            location.href = "/generos/"
        } else {
            swal.fire("Agregar Genero", resultado.mensaje, "warning")
        }
    })
    .catch(error => {
        console.error(error)
    })
}
function borrarGenero() {
    const genero = {
        nombre: document.getElementById('txtGenero').value
    }
    const url = "/genero/"

    fetch(url, {
        method: "DELETE",
        body: JSON.stringify(genero),
        headers: {
            "Content-Type": "application/json",
        }
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        if (resultado.estado) {
            location.href = "/generos/"
        } else {
            swal.fire("Agregar Genero", resultado.mensaje, "warning")
        }
    })
    .catch(error => {
        console.error(error)
    })
}

function agregarPelicula(){
    url = "/pelicula/"
    const pelicula={
        codigo: document.getElementById('txtCodigo').value,
        titulo: document.getElementById('txtTitulo').value,
        protagonista: document.getElementById('txtProtagonista').value,
        duracion: document.getElementById('txtDuracion').value,
        resumen: document.getElementById('txtResumen').value,
        genero: document.getElementById('cbGenero').value,
        foto: ''
    }
    fetch(url, {
        method: "POST",
        body: JSON.stringify(pelicula),
        headers: {
            "Content-Type": "application/json",
        }
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        if (resultado.estado) {
            location.href = "/peliculas/"
        }else{
            swal.fire("Agregar Pelicula", resultado.mensaje, "warning")
        }
    })
    .catch(error => {
        console.error(error)
    })
}

function validarPelicula(){
    if (document.getElementById("txtCodigo").value==""){
        mensaje="Debe ingresar código de la Película"
        return false;
    }else if(document.getElementById("txtTitulo").value==""){
        mensaje="Debe ingresar Titulo de la Película"
        return false;
    }else if(document.getElementById("txtProtagonista").value==""){
        mensaje="Debe ingresar el Protagonista de la Película"
        return false;
    }else if(document.getElementById("txtDuracion").value==""){
        mensaje="Debe ingresar la duración de la Película"
        return false;
    }else if(document.getElementById("cbGenero").value==""){
        mensaje="Debe seleccionar el género de la Película"
        return false;
    }else if(document.getElementById("txtResumen").value==""){
        mensaje="Debe ingresar un pequeño resumen de la Película"
        return false;
    }else{
        return true;
    }
}   
function editarPelicula(id){
    if(validarPelicula()){
        const pelicula={
            id:id,
            codigo:document.getElementById('txtCodigo').value,
            titulo:document.getElementById('txtTitulo').value,
            protagonista:document.getElementById('txtProtagonista').value,
            duracion:document.getElementById('txtDuracion').value,
            resumen:document.getElementById('txtResumen').value,
            genero:document.getElementById('cbGenero').value,
            foto:('')
        }
        const url="/pelicula/"
        fetch(url, {
            method: "PUT",
            body: JSON.stringify(pelicula),
            headers: {
                "Content-Type": "application/json",
            }
        })
        .then(respuesta => respuesta.json())
        .then(resultado=>{
            if(resultado.estado){
                location.href="/peliculas/"
            }else{
                swal.fire("edit pelicula",resultado.mensaje,"warning")

            }
        })
        .catch(error=>{
            console.error(error)
        })
    }else{
        swal.fire("Editar Pelicula", mensaje, "warning")
    }
    
}


   


/**
* 
* @param {*} id
*/
function deletePelicula(id){
    Swal.fire({
        title: "¿Está usted seguro de querer eliminar la Película?",
        showDenyButton: true,
        confirmButtonText: "SI",
        denyButtonText: "NO"
    }).then((result) => {
        if (result.isConfirmed) {
            const pelicula={
                id: id,
            }
            const url= "/pelicula/"
            fetch(url, {
                method: "DELETE",
                body: JSON.stringify(pelicula),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(respuesta => respuesta.json())
            .then(resultado => {
                if (resultado.estado){
                    location.href="/peliculas/"
                }else{
                    swal.fire("Delete Pelicula",resultado.mensaje,"warning")
                }
            })
            .catch(error => {
                console.error(error)
            })
        }
    });
}
function validarGenero(){
    if (document.getElementById("txtnombre").value==""){
        mensaje="Debe ingresar el nombre del género"
        return false;
    }else{
        return true;
    }
}


/**
* 
* @param {*} id
*/

function editarGenero(id){
    if(validarGenero()){
        const genero={
            id:id,
            nombre:document.getElementById('txtnombre').value,
           
        }
        const url="/genero/"
        fetch(url, {
            method: "PUT",
            body: JSON.stringify(genero),
            headers: {
                "Content-Type": "application/json",
            }
        })
        .then(respuesta => respuesta.json())
        .then(resultado=>{
            if(resultado.estado){
                location.href="/generos/"
            }else{
                swal.fire("edit generos",resultado.mensaje,"warning")

            }
        })
        .catch(error=>{
            console.error(error)
        })
    }else{
        swal.fire("Editar Generos", mensaje, "warning")
    }
    
}

/**
* 
* @param {*} id
*/
function deleteGenero(id){
    Swal.fire({
        title:"¿Está seguro de querer eliminar el género?",
        showDenyButton:true,
        confirmButtonText:"SI",
        denyButtonText:"NO"
    }).then((result)=>{
        if (result.isConfirmed){
            const genero= {
                id:id,
            }
            const ulr="/genero/"
            fecht(url, {
                method:"DELETE",
                body:JSON.stringify(genero),
                headers:{
                "Content-Type":"application/json"
                }
            })
            .then(respuesta => respuesta.json())
            .then(resultado=>{
                if (resultado.estado){
                    location.href="/generos/"
                }else{
                    swal.fire("Delete Genero",resultado.mensaje,"warning")
                }
            })
            .catch(error=>{
                console.error(error)
            })
        }
    });

}