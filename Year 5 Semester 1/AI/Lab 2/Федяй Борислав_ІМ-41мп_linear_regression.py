import numpy as np


def parameters_initialization(m):
    W = np.random.randn(1, m)
    b = 0.0
    return W, b


def forwardPropagate(X, W, b):
    if X.shape[0] != W.shape[1]:
        X = X.T

    z = np.dot(W, X) + b
    y_hat = z
    return z, y_hat


def cost(n, y_hat, y_true):

    J = (1 / n) * np.sum((y_hat - y_true) ** 2)
    return J


def backwardPropagate(n, X, y_hat, y_true):
    """
    Ця функція обчислює градієнти цільової функції відносно ваг та зсуву

    Параметри:
    n -- загальна кількість навчальних прикладів
    X -- вхідний вектор ознак форми (m, X_train.shape[1])
    y_hat -- вихідне значення лінійної регресії
    y_true -- істинне значення залежної змінної

    Повертає:
    dW -- градієнт цільової функції відносно ваг моделі
    db -- градієнт цільової функції відносно зсуву моделі
    """
    diff = y_hat - y_true
    
    if diff.shape[0] != 1:
        diff = diff.T
    
    if X.shape[0] != n:
        X = X.T
    
    dW = (2 / n) * np.dot(diff, X)
    
    db = (2 / n) * np.sum(diff)
    
    return dW, db


def update(alpha, dW, db, W, b):
    W = W - alpha * dW
    b = b - alpha * db
    
    return W, b

