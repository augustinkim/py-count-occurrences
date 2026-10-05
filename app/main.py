def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    
    lower = phrase.lower()
    return lower.count(letter.lower())
