import matplotlib.pyplot as plt, numpy as np

def f(x):
    return x**4 - 3 * x**3 + 2

def df(x):
    return 4 * x**3 - 9 * x**2

if __name__ == "__main__":
    x = np.arange(-5, 5, 0.2)
    y, y_dx = f(x), df(x)
    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].plot(x, y, color='mediumspringgreen')
    axarr[0].set_xlabel('x')
    axarr[0].set_ylabel('f(x)')
    axarr[0].set_title('f(x)')
    axarr[1].plot(x, y_dx, color='coral')
    axarr[1].set_xlabel('x')
    axarr[1].set_ylabel('dy/dx(x)')
    axarr[1].set_title('derivative of f(x)')
    axarr[2].set_xlabel('x')
    axarr[2].set_ylabel('GD')
    axarr[2].set_title('local minimum')
    iterations, cur_x, gamma, precision = 0, 6, 0.01, 0.00001
    previous_step_size = cur_x
    while previous_step_size > precision:
        prev_x = cur_x
        cur_x += -gamma * df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        iterations += 1
        axarr[2].plot(prev_x, cur_x, "o")
    f.subplots_adjust(hspace=0.3)
    f.tight_layout()
    plt.show()
    print ('minimum:', cur_x, '\niterations:', iterations)
