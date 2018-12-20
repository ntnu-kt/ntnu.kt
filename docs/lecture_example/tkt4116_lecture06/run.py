import ntnu.kt.course.tkt4116.lecture06 as lecture

# Now, what does the lecture say?

print(lecture.TASK)

# We assign q and L as constants, and use them later.

q = 1
L = 1

# Now, we can apply them.

F = q * L
R_tot = F + q * 2 * L

# Compute B by requiring moment equilibrium around A
M_A = q * 2*L * L + F * 3*L

# B_y must balance M_A

B_y = M_A / (2 * L)

# We can find A_y by requiring total vertical force equilibrium

A_y = R_tot - B_y

# print(A_y, B_y)
# =>
# 0.5 2.5

# A_y is quite a bit smaller than B_y, as expected.

# As we now have all the forces, we can compute the shear force diagram.

def V(x):
    """
    x = 0 in A
    Positive direction: ↓▯↑
    """
    if x <= 2 * L:
        return -A_y + q*x
    elif x <= 3*L:
        return -A_y + q*2*L - B_y

# Check: values in 0, 2*L and 3*L

# print(V(0.1))   # Just after A, about the same as A
# print(V(1.9*L)) # Just before B
# print(V(2.1*L)) # Just after B. Delta is 2.4, about the same as B_y (2.5)
# print(V(2.9*L)) # Just before F

def M(x):
    """
    x = 0 in A
    positive moment: ⤸▯⤹
    """
    if x <= 2 * L:
        return -A_y*x + q*x*x/2
    elif x <= 3 * L:
        return -A_y*x + q* 2*L * (x - L) - B_y * (x - 2*L)

# Check: values in 0, 2*L and 3*L

# # Around A, the moment is about zero.
# print(M(0.1*L))

# # In B, the moment is F * L = qL^2 = 1
# print(M(1.99*L))
# print(M(2.01*L)) # Check both sides - should be continuous

# # In C, the moment is 0.
# print(M(3*L))
