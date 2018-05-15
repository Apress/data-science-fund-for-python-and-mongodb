import matplotlib.pyplot as plt, numpy as np

def demand():
    p = np.random.uniform(0,1)
    if p < 0.10:
        return 10000
    elif p >= 0.10 and p < 0.45:
        return 20000
    elif p >= 0.45 and p < 0.75:
        return 40000
    else:
        return 60000

def production(demand, units, price, unit_cost, disposal):
    units_sold = min(units, demand)
    revenue = units_sold * price
    total_cost = units * unit_cost
    units_not_sold = units - demand
    if units_not_sold > 0:
        disposal_cost = disposal * units_not_sold
    else:
        disposal_cost = 0
    profit = revenue - total_cost - disposal_cost
    return profit

def mcs(x, n, units, price, unit_cost, disposal):
    profit = []
    while x <= n:
        d = demand()
        v = production(d, units, price, unit_cost, disposal)
        profit.append(v)
        x += 1
    return profit
    
def max_bar(ls):
    tup = max(enumerate(ls))
    return tup[0] - 1

if __name__ == "__main__":
    units = [10000, 20000, 40000, 60000]
    price, unit_cost, disposal = 4, 1.5, 0.2
    avg_p = []
    x, n = 1, 10000
    profit_10 = mcs(x, n, units[0], price, unit_cost, disposal)
    avg_p.append(np.mean(profit_10))
    print ('Profit for {:,.0f}'.format(units[0]),
          'units: ${:,.2f}'.format(np.mean(profit_10)))
    profit_20 = mcs(x, n, units[1], price, unit_cost, disposal)
    avg_p.append(np.mean(np.mean(profit_20)))
    print ('Profit for {:,.0f}'.format(units[1]),
          'units: ${:,.2f}'.format(np.mean(profit_20)))
    profit_40 = mcs(x, n, units[2], price, unit_cost, disposal)
    avg_p.append(np.mean(profit_40))
    print ('Profit for {:,.0f}'.format(units[2]),
          'units: ${:,.2f}'.format(np.mean(profit_40)))
    profit_60 = mcs(x, n, units[3], price, unit_cost, disposal)
    avg_p.append(np.mean(profit_60))
    print ('Profit for {:,.0f}'.format(units[3]),
          'units: ${:,.2f}'.format(np.mean(profit_60)))
    labels = ['10000','20000','40000','60000']
    pos = np.arange(len(labels))
    width = 0.75 # set less than 1.0 for spaces between bins
    plt.figure(2)
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(labels)
    barlist = plt.bar(pos, avg_p, width, color='aquamarine')
    barlist[max_bar(avg_p)].set_color('orchid')
    plt.ylabel('Profit')
    plt.xlabel('Production Quantity')
    plt.title('Production Quantity by Demand')
    plt.show()
