function ceasarCypher(word, num) {
  let alphabet = "abcdefghijklmnopqrstuvwxyz";
  // let caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let newWord = "";
  for (let i = 0; i < word.length; i++) {
    let char = word[i];
    let index = alphabet.indexOf(char);
    let newIndex = (num + index) % 26;
  if (alphabet.indexOf(alphabet[newIndex]) > -1) {
       newWord += alphabet[newIndex];
  } 
  // else if (caps.indexOf(caps[newIndex]) > -1) {
  //     newWord += caps[newIndex];
  // } 
  else {
    newWord += char;
  }
  return newWord;
}

console.log("Boy! What a string!", -5)
console.log("Hello zach168! Yes here.", 5)
console.log("Hello Zach168! Yes here.", -5)