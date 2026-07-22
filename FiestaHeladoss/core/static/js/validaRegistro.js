$(document).ready(function() {
    $("#verificar").click(function() {
        if ($("#mis-datos").valid()) {
            alert('Usuario registrado');
        } else {
            alert('Error... verifique los datos ingresados');
        }
    });
});

$(function(){ 
    $("#mis-datos").validate({ 
        rules:{
            nom:{
                required:true
            },
            ape:{
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
            pass1:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:'#pass1'
            },
        },//rules
        messages:{
            nom:{
                required:'Debe ingresar un nombre..',
                minlength:'Caracteres insuficientes(3)..'
            },
            ape:{
                required:'Debe ingresar apellido..',
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
            },
            pass1:{
                required:'Ingrese una contraseña..',
                minlength:'Caracteres insuficientes(8)'
            },
            pass2:{
                required:'Ingrese una contraseña..',
                minlength:'Caracteres insuficientes(8)',
                equalTo:'Las contraseñas no son iguales'
            }
        }//messages


    });//fin-validate
 });//fin
