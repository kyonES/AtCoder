# ABC079C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c
abcd = input()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])
op = ["+", "-"]
for op1 in op:
    for op2 in op:
        for op3 in op:
            result = a
            if op1 == "+":
                result += +b
            else:
                result += -b
            if op2 == "+":
                result += +c
            else:
                result += -c
            if op3 == "+":
                result += +d
            else:
                result += -d
            if result == 7:
                print(f"{a}{op1}{b}{op2}{c}{op3}{d}=7")
                exit()
