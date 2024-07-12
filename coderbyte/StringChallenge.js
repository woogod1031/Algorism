function splitHTML(str) {
  const array = [];
  let stringArray = [];
  for (let i = 0; i < str.length; i++) {
    if (str[i] == "<") {
      if (stringArray.length > 0) {
        array.push(stringArray.join(""));
      }
      stringArray = ["<"];
    } else if (str[i] == ">") {
      stringArray.push(">");
      array.push(stringArray.join(""));
      stringArray = [];
    } else {
      stringArray.push(str[i]);
    }
  }
  if (stringArray.length > 0) {
    array.push(stringArray.join(""));
  }
  return array;
}

function StringChallenge(str) {
  const array = splitHTML(str);
  const stack = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i].includes("</")) {
      if (stack[stack.length - 1].slice(1, -1) == array[i].slice(2, -1)) {
        stack.pop();
      } else {
        const stringArr = stack[stack.length - 1].slice(1, -1).split("");

        return `${stringArr.reverse().join("")}:a20zyfpjct`;
      }
    } else if (array[i].includes("<")) {
      stack.push(array[i]);
    }
  }
  return true;
}

console.log(StringChallenge("<div><b><p>hello world</p></b></div>"));
