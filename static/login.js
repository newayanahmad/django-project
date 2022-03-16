register_form = document.getElementById('register');
login_form = document.getElementById('login');
register_btn = document.getElementsByClassName('register')[0];
login_btn = document.getElementsByClassName('login')[0];
function login() {
    document.getElementsByClassName('button-back')[0].style.marginLeft = '37px'
    document.getElementsByClassName('forms')[0].style.marginLeft = '0'
    document.getElementsByClassName('login-box')[0].style.height = '300px'
    window.history.pushState('login', 'login', 'login');
    console.log(' login working...');
}

function register() {
    window.history.pushState('register', 'Register', 'register');
    document.getElementsByClassName('login-box')[0].style.height = '470px'
    document.getElementsByClassName('button-back')[0].style.marginLeft = '147px'
    console.log(' register working...');
    document.getElementsByClassName('forms')[0].style.marginLeft = '-306px'
}





// fetch api

var btn=document.getElementById('btn');
btn.addEventListener('click', ()=>{
    console.log('button clicked');
    fetch('api').then((response)=>{
        return response;
    })
})