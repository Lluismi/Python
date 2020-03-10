from duplicate_list import duplicate_list

if __name__ == "__main__":
    
    assert  duplicate_list("din") == "((("
    assert  duplicate_list("recede") == "()()()"
    assert  duplicate_list("Success") == ")())())"
    assert  duplicate_list("(( @") == "))(("