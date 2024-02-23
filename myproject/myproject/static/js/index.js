var test = false
document.querySelector('h1').addEventListener('click',()=>{
    test = !test
    if (test){
        document.querySelector('body').style.background = "#000"
    } else {
        document.querySelector('body').style.background = "rgb(87, 68, 44)"
    }
})