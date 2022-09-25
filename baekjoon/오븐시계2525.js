import fs from "fs";

let input = fs.readFileSync("예제.txt").toString().split("\n");
let now = input[0].split(" ").map((param) => Number(param));
let need = input[1];

function solution(now, need) {
  let hour = parseInt(need / 60);
  let min = need % 60;
  for (let i = 0; i < hour; i++) {
    now[0] = now[0] + 1 >= 24 ? 0 : now[0] + 1;
  }

  now[0] =
    now[0] + parseInt((now[1] + min) / 60) >= 24
      ? 0
      : now[0] + parseInt((now[1] + min) / 60);
  now[1] = (now[1] + min) % 60;
  console.log(now[0], now[1]);
}

solution(now, need);
