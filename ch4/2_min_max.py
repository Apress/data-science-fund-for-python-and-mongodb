import matplotlib.pyplot as plt, numpy as np

def f(x):
    return x**3 - 6 * x**2 + 9 * x + 15

def df(x):
    return 3 * x**2 - 12 * x + 9

if __name__ == "__main__":
    x = np.arange(-0.5, 5, 0.2)
    y = f(x)
    plt.figure('f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f(x)')
    plt.plot(x, y, color='blueviolet')
    plt.figure('local minimum')
    plt.xlabel('x')
    plt.ylabel('GD')
    plt.title('local minimum')
    iterations, cur_x, gamma, precision = 0, 6, 0.01, 0.00001
    previous_step_size = cur_x
    while previous_step_size > precision:
        prev_x = cur_x
        cur_x += -gamma * df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        iterations += 1
        plt.plot(prev_x, cur_x, "o")
    local_min = cur_x
    print ('minimum:', local_min, 'iterations:', iterations)
    plt.figure('local maximum')
    plt.xlabel('x')
    plt.ylabel('GD')
    plt.title('local maximum')
    iterations, cur_x, gamma, precision = 0, 0.5, 0.01, 0.00001
    previous_step_size = cur_x
    while previous_step_size > precision:
        prev_x = cur_x
        cur_x += -gamma * -df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        iterations += 1
        plt.plot(prev_x, cur_x, "o")
    local_max = cur_x
    print ('maximum:', local_max, 'iterations:', iterations)
    plt.show()
