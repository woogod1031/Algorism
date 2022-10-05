import fs from "fs";

let input = fs.readFileSync("예제.txt").toString().split("\n");
let now = input[0].split(" ").map((param) => +param);
let need = +input[1];

function solution(now, need) {
  let time = [now[0], now[1] + need];
  if (time[1] >= 60) {
    time[0] += parseInt(time[1] / 60);
    time[0] %= 24;
    time[1] %= 60;
  }
  console.log(time.join(" "));
}

solution(now, need);
