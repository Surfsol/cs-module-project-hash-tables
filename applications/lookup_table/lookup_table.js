//Your code here


cache = {}



function slowfun_too_slow(x, y){
    v = Math.pow(x, y)
    //v = Math.factorial(v)
    v /= Math.floor(x + y)
    v %= 982451653

    return v
}

for (let y=3; y<6; y++){
    for (let x=3; x<6; x++){
        cache[x.toString()+','+y.toString()] = slowfun_too_slow(x,y)
    }
}
    
        
   
console.log(cache)

// def slowfun(x, y):
//     """
//     Rewrite slowfun_too_slow() in here so that the program produces the same
//     output, but completes quickly instead of taking ages to run.
//     """
//     # Your code here
//     idx = str(x)+','+str(y)
//     if idx in cache:
//         return cache[idx]
//     else:
//         print('no values', x, y)


// # # # Do not modify below this line!

// for i in range(5000):
//     x = random.randrange(2, 14)
//     y = random.randrange(3, 6)
//     print(f'{i}: {x},{y}: {slowfun(x, y)}')