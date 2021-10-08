function reverseText() {
    let txtIn = document.getElementById("txtIn").value;
    document.getElementById("txtOut").innerHTML = txtIn.split("").reverse().join("");
}
document.getElementById("btnReverse").addEventListener("click", reverseText);