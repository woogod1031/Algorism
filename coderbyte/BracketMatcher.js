function BracketMatcher(str) {
  const regex = new RegExp("[()]", "g");
  const result = str.match(regex);
  let stack = [];

  result?.forEach((v) => {
    if (stack.length == 0) stack.push(v);
    else {
      if (v == ")" && stack[stack.length - 1] == "(") {
        stack.pop();
      } else {
        stack.push(v);
      }
    }
  });

  if (stack.length >= 1) return 0;
  return 1;
}

// keep this function call here
console.log(BracketMatcher("dogs and cats"));
