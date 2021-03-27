//About Button Line

let about = document.querySelector('.about')
let underLiner = document.querySelector('.aboutUnder')

about.addEventListener("mouseover", event=> {
  underLiner.style.width = "95px"
  underLiner.style.left = "0px"
});

about.addEventListener("mouseout", event=> {
  underLiner.style.width = "30px"
  underLiner.style.left = "30px"
});


