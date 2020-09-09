def word_count(s):
    
    dont_include = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    d = {}

    for x in s.lower().split():
        if x not in dont_include and d.get(x) == None:
            d[x] = 1
        else:
            d[x] += 1
    
    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))