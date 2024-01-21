const searchfields = document.querySelector('#searchfield');

searchfields.addEventListener('keyup',(e)=>{

    const searchValue = e.target.value;
    if(searchValue.trim().length>0){
        console.log('searchvalue',searchValue)



        fetch('/search-expenses',{
            body:JSON.stringify({searchText:searchValue}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data)
        
        })
    }

})