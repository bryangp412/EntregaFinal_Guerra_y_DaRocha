function ConfirmDelete()
{
    var respuesta = confirm("¿Estás seguro que deseas eliminar elemento seleccionado?")
    
    if(respuesta==true){
        return true
    }
    else{
        return false
    }
}

function ConfirmEdit()
{
    var respuesta = confirm("¿Estás seguro de editar los datos?")

    if(respuesta==true){
        return true
    }
    else{
        return false
    }
}

function CancelEdit()
{
    var respuesta = confirm("¿Estás seguro de cancelar la edición?")

    if(respuesta==true){
        return true
    }
    else{
        return false
    }
}