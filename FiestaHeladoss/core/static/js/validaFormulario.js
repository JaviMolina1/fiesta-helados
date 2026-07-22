$(function(){ 
    $("#mis-datos").validate({ 
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            telefono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
        },//rules
        messages:{
            nom:{
                required:'Debe ingresar un nombre..',
                minlength:'Caracteres insuficientes(3)..'
            },
            correo:{
                required:'Debe ingresar un correo electrónico',
                email:'Debe tener un formato válido de correo'
            },
            telefono:{
                required:'Ingrese un número de teléfono',
                number:'Ingrese un número válido',
                minlength:'Digitos insuficientes'
            },
            fecha:{
                required:'Seleccione su fecha de nacimiento',
                min:'Ingrese una fecha válida'
            }
            
        }//messages



    });//fin-validate
 });//fin

 