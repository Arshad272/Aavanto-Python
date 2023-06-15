# Bitwise Operators
# Bitwise operators perform operations in binary level

a = 3
b = 2

# biwise and => &
# 3 = 0 0 1 1
# 2 = 0 0 1 0
# --------------
# & = 0 0 1 0    => 2
# print( a & b ) 

# biwise or => "|" 
# 3 = 0 0 1 1
# 2 = 0 0 1 0
# --------------
# | = 0 0 1 1 => 3
# print(a | b)

# bitwise not operaor => ~
x = 2
# 2 = 0 0 1 0
# ------------
# ~ = 1 1 0 1
# print(~x)

# XOR operator '^' = shift + 6
# 3 = 0 0 1 1
# 2 = 0 0 1 0
# --------------
# ^ = 0 0 0 1   => 1
# print(a ^ b)

# Left Shift => '<<' 
# 3 = 0 0 1 1
# 2 = 0 0 1 0
# --------------
# <<=  1 1 0 0  => 12
# print(a << b)

# Right Shift Operator => '>>'
# 8 = 1 0 0 0
# 2 = 0 0 1 0
# --------------
# >>= 0 0 1 0 => 2
# print(8 >> 2)


a = 3
b = 2
a &= b
# a = a & b
print(a)