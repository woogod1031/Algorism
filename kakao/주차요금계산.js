function solution(fees = [], records = []) {
  const [d_time, d_cost, m_t, m_cost] = fees;
  const last_min = 1439;

  const map = new Map();

  records.forEach((val) => {
    const [time, _id, type] = val.split(" ");
    const [_hour, _min] = time.split(":").map((v) => Number(v));
    const total_min = _hour * 60 + _min;

    const current_time = map.get(_id);
    if (!current_time) map.set(_id, 0);

    const n_current_time = map.get(_id);
    if (type === "IN") map.set(_id, n_current_time + (last_min - total_min));
    if (type === "OUT") map.set(_id, n_current_time - (last_min - total_min));
  });

  const answer = [];

  for (let [car, _time] of map) {
    if (_time <= d_time) _time = d_cost;
    else _time = Math.ceil((_time - d_time) / m_t) * m_cost + d_cost;
    answer.push([car, _time]);
  }

  return answer.sort((a, b) => a[0] - b[0]).map((v) => v[1]);
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
