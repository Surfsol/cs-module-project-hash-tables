#ignore = [" : ; , . - + = / \ | [ ] { } ( ) * ^ &]
cache = {}
def word_count(s):
    # Your code here
    # split on white space
    apart = s.split()
    for s in apart:
        print(s)
    #print(s)
    #make words lower case
    #use a cache
word_count('Hello, my cat. And my cat doesn\'t say "hello" back.')


# if __name__ == "__main__":
#     print(word_count(""))
#     print(word_count("Hello"))
#     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))