function solution(cacheSize, cities) {
  const MISS = 5;
  const HIT = 1;

  let time = 0;
  let cache = [];

  function isCache(city) {
    const cityIndex = cache.findIndex((c) => c == city);
    if (cityIndex !== -1) {
      cache = [...cache.filter((_, idx) => idx !== cityIndex), city];
      return HIT;
    } else {
      if (cacheSize > 0) {
        if (cache.length >= cacheSize) {
          cache.shift();
        }
        cache.push(city);
      }
      return MISS;
    }
  }

  cities.forEach((city) => {
    city = city.toUpperCase();
    time += isCache(city);
  });

  return time;
}

console.log(solution(0, ["Jeju", "Jeju"]));
