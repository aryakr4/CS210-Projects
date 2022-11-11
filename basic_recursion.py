def bowtie(length: int):
    # base case (if length <=0, nothing happens)
    if length == 1:
        print('*' * length)
    else:
        print('*' * length)
        bowtie(length - 1)
        print('*' * length)
            
    
def check_vowel(letter: str)-> int:
    """
    Returns 1 if given letter is a vowel, 0 otherwise
    """
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        return 1
    return 0

def count_vowels(string: str) -> int:
    """
    Returns count of vowels in the given string

    >>> count_vowels('abc de')
    2
    >>> count_vowels('Hi Everyone!')
    5
    """
    if string == "":
        return 0
    elif check_vowel(string[0]) == 1:
        return 1 + count_vowels(string[1:])
    else:
        return 0 + count_vowels(string[1:])
        
