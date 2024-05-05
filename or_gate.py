def perceptron_AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 # w1,w2는 가중치 / theta는 임계값
    result = w1 * x1 + w2 * x2 # 인풋값과 가중치 곱의 덧셈이 임계값 이상일때 값을 1로 바꿈 아니면 0으로 바꿈
    if result >= theta:
        return 1
    else:
        return 0


print(perceptron_AND(0, 0))  #Result = 0
print(perceptron_AND(1, 0))  #Result = 0
print(perceptron_AND(0, 1))  #Result = 0
print(perceptron_AND(1, 1))  #Result = 1
