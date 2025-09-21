# Robot Vacuum (From 2021 Australian Informatics Olympiad)
# C/C++/Python/Java
# Time and Memory Limits: 1 second, 1 GB
# Medium Question

# Irene has a robot vacuum cleaner that automatically cleans her floor. 
# Each day, the robot performs the same sequence of K instructions.
# There are four possible instructions, each represented by an uppercase character.
# Each instruction moves the robot one step in one of the four cardinal directions:
# • N - the robot moves one step north (↑).
# • E - the robot moves one step east (→).
# • S - the robot moves one step south (↓).
# • W - the robot moves one step west (←).

# After the sequence of K instructions, the robot is supposed to finish where it started,
# but the original programmers were a little bit rushed.
# Irene has asked for your programming help. What is the smallest number of instructions needed
# to add to the end of the sequence so that the robot finishes where it started?

# Input
# • The first line of input contains the single integer K.
# • The second line of input contains a string of K characters, the sequence of instructions.

# Output
# Your program should output a single integer, the fewest instructions you need to add to the end of the sequence.

# Sample Input 1
# 5
# ENNEE
# Sample Output 1
# 5
# Sample Input 2
# 7
# EEWWWWE
# Sample Output 2
# 1
# Sample Input 3
# 8
# SWWNENNS
# Sample Output 3
# 2

#vvvvvvvvvvvvvvvvvv Solution Below vvvvvvvvvvvvvvvvvvv

K = int(input())
ins = input().strip()
x = 0
y = 0

for i in range(K):
    if ins[i] == 'N':
        y += 1
    elif ins[i] == 'E':
        x += 1
    elif ins[i] == 'S':
        y -= 1
    elif ins[i] == 'W':
        x -= 1

print(abs(x)+abs(y))

# Time : 0.047s
# Memory : 3.8 MiB
# Results : 100/100
