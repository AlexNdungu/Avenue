let wordStatus = true;

let emoji = function () {
    let emog = document.querySelectorAll('.adm_go #reps');
    let word = document.querySelectorAll('.adm_go ul li span');
    let navi = document.querySelector('.admin_nav');
    let logo = document.querySelector('.logo');
    let bagger = document.querySelector('.admBager');
    let emoSty = document.querySelectorAll('.adm_go ul li');
    let topNav = document.querySelector('.pic_navigation');

    if( wordStatus === true){
        word.forEach(e => e.style.display = "none");
        emog.forEach(e => e.style.fontSize = "32px");
        navi.style.width = "100px";
        logo.style.display = "none"
        bagger.style.marginRight = "40px";
        emoSty.forEach(e => e.style.marginLeft = "32%");
        topNav.classList.toggle("used")

        wordStatus = false;
    }

    else if( wordStatus === false){
        word.forEach(e => e.style.display = "inline");
        emog.forEach(e => e.style.fontSize = "23px");
        navi.style.width = "280px";
        logo.style.display = "inline"
        bagger.style.marginRight = "20px";
        emoSty.forEach(e => e.style.marginLeft = "6%");
        topNav.classList.toggle("normal")
        topNav.classList.remove("used")

        wordStatus = true;
    }
}