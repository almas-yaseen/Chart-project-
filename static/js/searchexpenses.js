const searchfields = document.querySelector('#searchfield');
const apptable = document.querySelector('.app-table')

const paginationcontainer = document.querySelector('.pagination-container');
tableoutput.style.display = "none;"


searchfields.addEventListener('keyup',(e)=>{

    const searchValue = e.target.value;
    if(searchValue.trim().length>0){
        paginationcontainer.style.display="none"
        console.log('searchvalue',searchValue)



        fetch('/search-expenses',{
            body:JSON.stringify({searchText:searchValue}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data)
            apptable.style.display = "none"
            tableoutput.style.display="block";
            if(data.length==0){
                tableoutput.innerHTML = 'No results found'

             



            }

        
        })
    }else{
        tableoutput.style.display = "none"
        apptable.style.display="block"
        paginationcontainer.style.display = "block"

    }

})