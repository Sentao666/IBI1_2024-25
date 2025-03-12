# 创建布尔变量X并初始化为True
X = True
# 创建布尔变量Y并初始化为False
Y = False

# 创建变量W，表示X和Y的“与”关系
W = X and Y

# 打印变量W的值
print("W的值为:", W)

# 以注释形式给出W的真值表
# 真值表：
# | X | Y | W（X and Y）|
# |---|---|-------------|
# | T | T | T           |
# | T | F | F           |
# | F | T | F           |
# | F | F | F           |