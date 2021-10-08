function caesarEncrypt() {
  let symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
  let key = Math.abs(parseInt(document.getElementById("keyIn").value));
  while (key>symbols.length) {
    key = key - symbols.length
  }
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

function caesarDecrypt() {
  let symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
  let key = Math.abs(parseInt(document.getElementById("keyIn").value));
  while (key>symbols.length) {
    key = key - symbols.length
  }
  let encryptedTxt = "";
  let txtIn = document.getElementById("txtIn").value.split("");
  txtIn.forEach((letter) => {
    indexold = symbols.indexOf(letter);
    indexnew = indexold - key;
    translatedLetter = symbols.charAt(indexnew);
    encryptedTxt = encryptedTxt + translatedLetter;
  });
  document.getElementById("txtOut").innerHTML = encryptedTxt;
}


document.getElementById("btn_encrypt").addEventListener("click", caesarEncrypt);
document.getElementById("btn_decrypt").addEventListener("click", caesarDecrypt);
