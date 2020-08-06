const string = 'The brown fox ran downtown'


//count numb of times letter occures
cache = {}
function count(s){
    arr = s.replace(/ /g,'')
    console.log(arr)
    arr = arr.split('')
    for(let i=0; i<arr.length; i++){
        if (!Object.keys(cache).includes(arr[i])){
            cache[arr[i]] = 1
        } else {
            cache[arr[i]] += 1
        }
    }
    console.log(cache)
}

console.log(count(string))


// str.trim() can only be used to 
// remove white space before and after a string, 
// to remove white space between the string, 
// we would have to be a bit more creative 
// and use str.split(‘ ’). join(‘’)