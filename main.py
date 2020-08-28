def is_palindrome(Text):
    #function compares given word with its reversed version
    return Text == ''.join(reversed(Text))
    
print(is_palindrome('lotol'))
