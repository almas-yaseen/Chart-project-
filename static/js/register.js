const usernameField = document.querySelector('#usernameField')
const feedback = document.querySelector('.invalid-feedback')
const emailField = document.querySelector('#emailfield')
const emailFeedbackArea = document.querySelector('.emailFeedBackArea')
const passwordfield = document.querySelector('#PasswordField')
const usernameSuccessOutput = document.querySelector('.usernamesuccessOutput')
const showpasstoggle = document.querySelector('.showPasswordToggle')
const submitBtn = document.querySelector('.submit-btn')



const handleToggleInput = (e) => {
    if(showpasstoggle.textContent==='SHOW'){
        showpasstoggle.textContent = 'HIDE'
        passwordfield.setAttribute("type","text");



    }else{
        passwordfield.setAttribute("type","password");
        showpasstoggle.textContent = 'SHOW'

    }

}
showpasstoggle.addEventListener('click',handleToggleInput);









emailField.addEventListener('keyup',(e)=>{
    const emailVal = e.target.value;

    
    emailField.classList.remove("is-invalid");
    emailFeedbackArea.style.display = "none"

    if(emailVal.length > 0 ){
        fetch('/authentication/validate-email',{
            body:JSON.stringify({email:emailVal }),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            
            if(data.email_error){
              
                submitBtn.disabled = true
                emailField.classList.add("is-invalid");
                emailFeedbackArea.style.display ='block'
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;


            }else{
                submitBtn.removeAttribute('disabled')

             

            }

        })
    
        
    }



})








usernameField.addEventListener('keyup',(e)=>{
    console.log('777',7777);
    const usernameVal = e.target.value;
    usernameSuccessOutput.style.display = "block"
    usernameSuccessOutput.textContent =`Checking  ${usernameVal}`

    usernameField.classList.remove("is-invalid");
    feedback.style.display ='none'
    




    if(usernameVal.length > 0 ){
        fetch('/authentication/validate-username',{
            body:JSON.stringify({username:usernameVal}),
            method:"POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data",data);
            usernameSuccessOutput.style.display ='none'
            if(data.username_error){
                usernameField.classList.add("is-invalid");
                feedback.style.display ='block';
                feedback.innerHTML = `<p>${data.username_error}</p>`
                submitBtn.disabled = true;


            }else{
                 submitBtn.removeAttribute('disabled')
            }
        })
    
        
    }

    })
  