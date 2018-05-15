import matplotlib.pyplot as plt, numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def df(x):
    return x * (1-x)

if __name__ == "__main__":
    x = np.arange(-10., 10., 0.2)
    y, y_dx = sigmoid(x), df(x)
    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].plot(x, y, color='lime')
    axarr[0].set_xlabel('x')
    axarr[0].set_ylabel('f(x)')
    axarr[0].set_title('Sigmoid Function')
    axarr[1].plot(x, y_dx, color='coral')
    axarr[1].set_xlabel('x')
    axarr[1].set_ylabel('dy/dx(x)')
    axarr[1].set_title('Derivative of f(x)')
    axarr[2].set_xlabel('x')
    axarr[2].set_ylabel('GD')
    axarr[2].set_title('local maximum')
    iterations, cur_x, gamma, precision = 0, 0.01, 0.01, 0.00001
    previous_step_size = cur_x
    while previous_step_size > precision:
        prev_x = cur_x
        cur_x += -gamma * -df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        iterations += 1
        plt.plot(prev_x, cur_x, "o")    
    f.subplots_adjust(hspace=0.3)
    f.tight_layout()
    print ('maximum:', cur_x, '\niterations:', iterations)
    plt.show()
