const usernameField = document.querySelector('#usernameField')
const feedback = document.querySelector('.invalid-feedback')


usernameField.addEventListener('keyup',(e)=>{
    console.log('777',7777);
    const usernameVal = e.target.value;

    usernameField.classList.remove("is-invalid");
    feedback.style.display ='none'
    




    if(usernameVal.length>0 ){
        fetch('/authentication/validate-username',{
            body:JSON.stringify({username:usernameVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            if(data.username_error){
                usernameField.classList.add("is-invalid");
                feedback.style.display ='block'
                feedback.innerHTML = `<p>${data.username_error}</p>`


            }

        })
    
        
    }

    })
  