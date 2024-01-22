const searchfields = document.querySelector('#searchfield');
const tableoutput = document.querySelector('.table-output')
const apptable = document.querySelector('.app-table')
const paginationcontainer  = document.querySelector('.pagination-container')

const tablebodys = document.querySelector('.table-body')

searchfields.addEventListener('keyup',(e)=>{

    const searchValue = e.target.value;
    if(searchValue.trim().length > 0){
        paginationcontainer.style.display = "none"
        tablebodys.innerHTML = ""
        
        

        console.log('searchvalue',searchValue)



        fetch('/search-expenses',{
            body:JSON.stringify({searchText:searchValue}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data)
            apptable.style.display = "none"
            tableoutput.style.display  = "block"

            if(data.length === 0){

                tableoutput.innerHTML = 'No results found'

            }else{
                data.forEach((item) => {
                    tablebodys.innerHTML += `<tr>
                    <td>${item.amount}</td>
                    <td>${item.category}</td>
                    <td>${item.description}</td>
                    <td>${item.date}</td>
                    
                    </tr>`
                    
                });

            }


        })
    }else{
        apptable.style.display = "block";
        paginationcontainer.style.display = "block"
        tableoutput.style.dipslay = "none"

    }
})