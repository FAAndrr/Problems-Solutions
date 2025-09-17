# Palindrome C++/C/Python/Java 
# (Python3 solution)
# Easy question

# A palindrome is a word that is the same when read forwards and backwards, for example madam, racecar, and deed.
# You will be given a word with N lowercase letters, which may or may not be a palindrome. 
# Your goal is to change this word into a palindrome. 
# You cannot add or remove letters; you can only change existing ones.
# You want to transform the word into a palindrome by making the fewest number of letter changes. 
# If multiple palindromes can be made with the fewest number of changes, you should choose the one that is alphabetically smallest.
# --------------------------------------------------------------------
# The first line of input contains the integer N, the length of the word.
# The second line of input contains a word consisting of N lowercase letters.
# It is guaranteed that 2 ≤ N ≤ 100 000.
# We strongly recommend using the solution templates provided below. These templates will ensure that you handle the input and output correctly.
# --------------------------------------------------------------------
# Your output should be a palindrome with N lowercase letters, which is the alphabetically smallest palindrome possible with the fewest number of changes.
# Sample Input 1
# racecab
# Sample Output 1
# bacecab
# --------------------------------------------------------------------
# Explanation 1
# By changing 1 letter, you can make either of the following two palindromes:
# • bacecab
# • racecar
# Since bacecab is alphabetically smaller, it is the correct answer.
# Sample Input 2
# • deed
# Sample Output 2
# • deed
# Explanation 2
# The word deed is already a palindrome, so no changes are necessary.
# --------------------------------------------------------------------

# vvvvvvvvvvvvvvvvvvvvvvv Solution below vvvvvvvvvvvvvvvvvvvvvvvvvvvvv

_ = input()
word = input()
char = list(word.strip())
for i in range(len(char)//2):
    j = len(char) - 1 - i
    char[i] = char[j] = min(char[i], char[j])  
print("".join(char))
