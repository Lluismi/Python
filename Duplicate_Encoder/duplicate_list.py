from collections import Counter

def duplicate_list(word):
    word = word.lower()
    new_string = ''
    count = Counter(word)
    for x in word:
        if count[x] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string

if __name__ == "__main__":
    
    assert  duplicate_list("din") == "((("
    assert  duplicate_list("recede") == "()()()"
    assert  duplicate_list("Success") == ")())())"
    assert  duplicate_list("(( @") == "))(("