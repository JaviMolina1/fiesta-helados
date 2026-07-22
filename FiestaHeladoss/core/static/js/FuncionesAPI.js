
function mostrarPrecios(){
    let url='http://localhost:3300/Precios';
    fetch(url)
    .then(response => response.json())
    .then(data => PreciosData(data))
    .catch(error => console.log(error))

    const PreciosData=(data)=>{
        console.log(data);
        let texto="";

        for(i=0; i<data.length; i++){
            texto+=`<tr>
                <td>${data[i].id}</td>
                <td>${data[i].Rango}</td>
                <td>${data[i].Precio}</td>
                <td>${data[i].Sabores}</td>
                </tr>`
        }
        document.getElementById('valores').innerHTML=texto;
    }
}