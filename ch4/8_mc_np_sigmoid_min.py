import random, numpy as np

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sigmoid_gradient(v):
    return [v_i * (1-v_i) for v_i in v]

def round_v(v):
    return np.round(v, decimals=3)

if __name__ == "__main__":
    trials= 10
    sims = 10
    avg_its = []
    for _ in range(trials):
        its = []        
        for _ in range(sims):
            v = [random.randint(-10, 10) for i in range(3)]
            tolerance = 0.0000001
            iterations = 0
            while True:
                gradient = sigmoid_gradient(v)
                next_v = step(v, gradient, -0.01)
                norm_v = np.linalg.norm(v)
                norm_next_v = np.linalg.norm(next_v)
                test_v = norm_v - norm_next_v
                if test_v < tolerance:
                    break
                v = next_v
                iterations += 1
            its.append(iterations)
        a = round(np.mean(its))
        avg_its.append(a)
    gap = np.max(avg_its) - np.min(avg_its)
    print (trials, 'trials with', sims, 'simulations each:')
    print ('gap', gap)
    print ('avg iterations', round(np.mean(avg_its)))
