function solution(s) {
  const regex = /0/g;

  function rc(_str, _cnt, _zero_cnt) {
    if (_str !== "1") {
      const _len = _str.length;
      const _s = _str.replace(regex, "").length;
      return rc(_s.toString(2), _cnt + 1, _zero_cnt + _len - _s);
    }
    return [_cnt, _zero_cnt];
  }

  const result = rc(s, 0, 0);

  return result;
}

console.log(solution("110010101001"));
