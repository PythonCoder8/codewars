function digital_root(n) {
  var sumOfNums = 0;
  var arrOfNums = n.toString().split("").map(function(str) {  // [ 9, 4, 2 ]
    return parseInt(str); 
  });
  while (arrOfNums.length > 1) {
    sumOfNums = arrOfNums.reduce(function(a, b) { // 15
      return a + b;
    });
    arrOfNums = sumOfNums.toString().split("").map(function(str) { // turns 15 into [1, 5]
    return parseInt(str);
    });
  }
  return sumOfNums;
}
