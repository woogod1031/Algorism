if (
  watchAllField.level -
  [watchAllField.depth_1, watchAllField.depth_2, watchAllField.depth_3].reduce(
    (p, c) => p + !!c,
    0
  )
) {
  return setIsEmpty(true);
} else {
  setIsSave(true);
}
//우선 0이면 setIsSave, 0이 아니면 setIsEmpty

//level 단계가 1,2,3 단계가 있을 때
//1단계는 depth_1만 존재하면되고
//2단계는 depth_1과 depth_2 두개만 존재하면되고
//3단계는 depth_1과 depth_2,depth_2 모두 존재해야할때

//level의 단계가 뭔지에 따라서 어떻게 조건(depth에 값이 있는지)을 검사할 것인가

//level(1 or 2 or 3)에서
//reduce를 통해 각 depth의 유무를 구한다.

//만약 각 depth가 모두 존재 하지 않으면 0을 return 한다.
//하나만 존재하면 1만 리턴
//두개가 존재하면 2만 리턴
//세개가 존재하면 3을 리턴

//만약 level이 3일 때 두 depth만 값이 들어있다면,
//3(level) - (0 + 0 + 1) = 2
//값이 0이 아니라는건 아직 다른 빈 값이 남았다는 것
//만약 level이 3일때 depth가 3개 다 있으면
//3 - 3 = 0으로 setI
