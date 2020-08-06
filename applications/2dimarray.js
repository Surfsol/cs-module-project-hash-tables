// Add up and print the sum of the all of the minimum elements of each inner array:
// [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
// You may use whatever programming language you’d like.
// Verbalize your thought process as much as possible before writing any code.
// Utilize UPER while going through thought process.

function min(A) {
  //iterate array
  //take min of each array
  //make a counter starting from 0, add each min value
  count = 0;
  for (let i = 0; i < A.length; i++) {
    // spread in array
    count += Math.min(...A[i]);
  }
  return count;
}
A = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]];
console.log(min(A));
