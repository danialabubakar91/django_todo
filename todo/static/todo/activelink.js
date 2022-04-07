// Add active class to the current link(highlight it)
const todoNav = document.getElementById("todoNav");
const navLink = todoNav.getElementsByClassName("nav-link");
for (let item of navLink) {
    item.addEventListener("click", function(){
        const current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

