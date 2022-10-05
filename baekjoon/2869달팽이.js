import fs from "fs";

let input = fs
  .readFileSync("예제.txt")
  .toString()
  .split(" ")
  .map((num) => Number(num));

const A = input[0];
const B = input[1];
const V = input[2];

console.log(Math.ceil((V - B) / (A - B)));
