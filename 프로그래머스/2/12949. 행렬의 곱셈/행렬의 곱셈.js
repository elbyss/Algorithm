function solution(arr1, arr2) {
    const answer = Array.from({ length: arr1.length }, () => 
    Array.from({ length: arr2[0].length }, () => 0)
  );

  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2[0].length; j++) {
      for (let k = 0; k < arr1[0].length; k++) {
        answer[i][j] += arr1[i][k] * arr2[k][j];
      }
    }
  }
  
  console.log(answer);
  return answer;
}