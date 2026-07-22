function mostrarFeriados(){
    let url='https://api.boostr.cl/holidays.json';
    fetch(url)
    .then(response => response.json())
    .then(data => mostrarFeriados(data))
    .catch(error => console.log(error))

    const mostrarFeriados=(data)=>{
        console.log(data)
        let body=""
        for(var i=0; i<data.data.length; i++)
        {
            if (i == 1 || i == 3 || i == 5 || i == 7 || i == 9 || i == 11 || i == 13 || i == 15 || i == 17 || i == 19){
                body+=`<td>-------✅-------</td>
                <td>${data.data[i].date}</td>
                <td>${data.data[i].title}</td>
                `
            }
            else{
                body+=`<tr>
                <td>-------❌-------</td>
                    <td>${data.data[i].date}</td>
                    <td>${data.data[i].title}</td>
                    
                    </tr>`
            }
        }
        document.getElementById('feriados').innerHTML=body;


    }
}