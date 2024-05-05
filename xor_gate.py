import numpy as np # 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 대표적인 파이썬의 딥러닝 라이브러리

# NAND 게이트
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 가중치
    b = 0.7  # 임계값
    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

# OR 게이트
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.2  # 임계값
    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

# AND 게이트
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.7  # 임계값
    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

# XOR 게이트 (다층 퍼셉트론)
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# 테스트
print("XOR(0, 0):", XOR(0, 0)) #Result = 0
print("XOR(1, 0):", XOR(1, 0)) #Result = 1
print("XOR(0, 1):", XOR(0, 1)) #Result = 1
print("XOR(1, 1):", XOR(1, 1)) #Result = 0
