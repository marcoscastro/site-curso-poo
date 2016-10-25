function validateForm() {
    var email = document.forms["formLead"]["email"].value;
    var atpos = email.indexOf("@");
    var dotpos = email.lastIndexOf(".");

    if (atpos < 1 || dotpos < atpos+2 || dotpos+2 >= email.length) {
        alert("Oops...você não digitou um e-mail válido :(");
        return false;
    }
}