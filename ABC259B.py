# ABC259B-Counterclockwise Rotation
# https://atcoder.jp/contests/abc259/tasks/abc259_b
import math
a, b, d = map(int, input().split())
d = math.pi/180*d
x = a*math.cos(d)-b*math.sin(d)
y = a*math.sin(d)+b*math.cos(d)
print(x, y)
