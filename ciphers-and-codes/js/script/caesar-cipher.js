function caesarEncrypt() {
  let symbols = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ0123456789";
  let key = parseInt(document.getElementById("keyIn").value);
  let encryptedTxt = "";
  let txtIn = document.getElementById("txtIn").value.split("");
  txtIn.forEach((letter) => {
    indexold = symbols.indexOf(letter);
    indexnew = indexold + key;
    translatedLetter = symbols.charAt(indexnew);
    encryptedTxt = encryptedTxt + translatedLetter;
  });
  document.getElementById("txtOut").innerHTML = encryptedTxt;
}
document.getElementById("submit").addEventListener("click", caesarEncrypt);
