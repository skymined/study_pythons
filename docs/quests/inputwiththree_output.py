#quest
#가로  * 세로 * 높이 = 직육면체
#input: 가로 세로 높이
#output: 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3

length, width, height = input().split()

length = int(length)
width = int(width)
height = int(height)

box= length*width*height

print("가로 ({})m * 세로({})m * 높이({})m = 직육면체({})m^3".format(length, width, height, box))