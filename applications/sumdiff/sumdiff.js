let sumA = {};
let dif = {};
function Alg(x){ return x * 4 + 6}
function sumDiff(A) {
  // match items in pairs and compare diff
  for (let i = 0; i < A.length; i++) {
    for (let j = 0; j < A.length; j++) {
      sumA[A[i].toString() +','+ A[j].toString()] = Alg(A[i]) + Alg(A[j]);
      dif[A[i].toString() +','+ A[j].toString()] = Alg(A[i]) - Alg(A[j]);
    }
  }
 // console.log(sumA, dif)
  keysA = Object.keys(sumA)
  for (let a in sumA){
    for (let b in dif){
        if ((sumA[a] - dif[b]) === 0){
           // arrA = Object.keys(sumA)[a]

            // console.log(a)
            console.log(b)
            a = a.split(/','+/)
            console.log(a)
            a1 = a[0].slice(1)
            console.log(a1)
         
        
            return `f(${a[0]}) + f(${a[2]}) = f(${b[0]}) + f(${b[-1]})`
        }
    }
  }

}
let arr = [1, 3, 4, 7, 12];
console.log(sumDiff(arr));
