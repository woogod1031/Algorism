function solution(fees = [], records = []) {
  const [d_time, d_cost, m_t, m_cost] = fees;
  const last_min = 23 * 60 + 59;

  const map = new Map();

  records.reverse().forEach((val) => {
    const [time, _id, method] = val.split(" ");
    const [_hour, _min] = time.split(":").map((v) => Number(v));
    const total_min = _hour * 60 + _min;
    const current_time = map.get(_id);
    if (method == "IN") {
      if (current_time) {
        map.set(_id, current_time - total_min);
      } else {
        map.set(_id, last_min - total_min);
      }
    } else {
      if (current_time) {
        map.set(_id, current_time + total_min);
      } else {
        map.set(_id, total_min);
      }
    }
  });

  const answer = Array.from(map, (val) => val).reduce((acc, [key, val]) => {
    const time =
      val - d_time > 0 ? Math.ceil((val - d_time) / m_t) * m_cost : 0;
    return {
      ...acc,
      [key]: d_cost + time,
    };
  }, {});

  return Object.entries(answer)
    .sort((a, b) => {
      return +a[0] - +b[0];
    })
    .map(([c, d]) => d);
}

console.log(
  solution(
    [180, 5000, 10, 600],
    [
      "05:34 5961 IN",
      "06:00 0000 IN",
      "06:34 0000 OUT",
      "07:59 5961 OUT",
      "07:59 0148 IN",
      "18:59 0000 IN",
      "19:09 0148 OUT",
      "22:59 5961 IN",
      "23:00 5961 OUT",
    ]
  )
);
