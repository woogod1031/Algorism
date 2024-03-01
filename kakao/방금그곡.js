function calc(start, end) {
  const [sh, sm] = start.split(":");
  const [eh, em] = end.split(":");
  let h = eh - sh;
  let m = em - sm;
  return h * 60 + m;
}

function replaceChar(str) {
  const result = str
    .replaceAll("C#", "H")
    .replaceAll("D#", "I")
    .replaceAll("F#", "J")
    .replaceAll("G#", "K")
    .replaceAll("A#", "L")
    .replaceAll("B#", "M");
  return result;
}
function solution(m, musicinfos) {
  m = replaceChar(m);
  musicinfos = musicinfos
    .map((m, i) => {
      const [startT, endT, name, code] = m.split(",");
      const time = calc(startT, endT);
      const totalCode = replaceChar(code);
      return [i, time, name, totalCode.padEnd(time, totalCode).slice(0, time)];
    })
    .filter(([_, __, ___, me]) => me.indexOf(m) >= 0)
    .sort(([i1, a], [i2, b]) => {
      if (a == b) {
        return i1 - i2;
      }
      return b - a;
    });

  return musicinfos[0]?.[2] || "(None)";
}
solution("ABC#DEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]);
