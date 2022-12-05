// const square_css = square_css_location.attributes.href.baseURI.split("/") 
const URL_path = window.location.href.split("/");

const URL_page = URL_path[URL_path.length - 1];
const ul_list = document.getElementById("ul_list")
// const URL_element = square_css[square_css.length -1]



for (let i = 0; i < ul_list.children.length; i++){
    if (ul_list.children[i].children[0].attributes[0].value == URL_page){
        ul_list.children[i].children[0].classList.add("is-current")
    } else {

        ul_list.children[0].children[0].classList.toggle("is-current")
    }
        
    

}
