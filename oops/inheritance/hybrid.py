class A:
    pass

class B:
    pass

class C:
    pass

class X(A, B, C):
    pass

class Y(B, C):
    pass

class Z(X, Y):
    pass

print(Z.mro())