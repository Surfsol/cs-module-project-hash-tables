//ignore = ['"', ':', ';', ',', '.','-', '+', '=', '/', '\' ,'|', '[', ']', '{', '}', '(',' )', '*', '^', '&']
ignore = [':', ';', ',', '.','-', '+', '=', '/']
let cache = {}
function  word_count(s){
    // Your code here
    // split on white space
    apart = s.replace(/.|,|""/g, "")
    apart = apart.split(/[ ]+/)
    for(let i=0; i<apart.length; i++){
        if (Object.keys(cache).includes(apart[i])){
            console.log('includes')
            cache[apart[i]] += 1
        } else {
            cache[apart[i]] = 1
        }
    }
    
    console.log(cache)
    //split(/[ ,]+/)
    

    //console.log(s.replace(ignore, ''))
    // apart = s.split(...ignore)
    // console.log(apart)
    // for s in apart:
    //     print(s)
    // #print(s)
    // #make words lower case
    // #use a cache
}
word_count('Hello, my cat. And my cat doesn\'t say "hello" back.')


// # if __name__ == "__main__":
// #     print(word_count(""))
// #     print(word_count("Hello"))
// #     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
// #     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))