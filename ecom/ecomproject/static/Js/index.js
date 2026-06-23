


function cat2() {
    alert("Function triggered!");
}

function menu() {
    var menu = document.getElementsByClassName('menu')[0];

    if (menu.style.display == 'block') {
        menu.style.display = 'none'
    }
    else {
        menu.style.display = 'block'
    }
}

function hello() {
    var removeAll = document.getElementsByClassName('menu')[0];
    removeAll.style.display = 'none';

    // var hello= document.getElementById('close')
    // close.onclick = function () {
    //     hello.remove()
    // }
}

