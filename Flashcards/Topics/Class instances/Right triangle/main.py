class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = 0.5 * leg_1 * leg_2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

if input_c * input_c == (input_a * input_a) + (input_b * input_b):
    triangle = RightTriangle(hyp=input_c,leg_1=input_a,leg_2=input_b)
    print(triangle.area)
else:
    print("Not right")

# write your code here