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

def display(p):
    print ('Profit for {:,.0f}'.format(units[1]),
           'units: ${:,.2f}'.format(np.mean(p)))
    
if __name__ == "__main__":
    units = [10000, 20000, 40000, 60000]
    price, unit_cost, disposal = 4, 1.5, 0.2
    avg_ls = []
    x, n, y, z = 1, 10000, 1, 1000
    while y <= z:
        profit_10 = mcs(x, n, units[0], price, unit_cost, disposal)
        profit_20 = mcs(x, n, units[1], price, unit_cost, disposal)
        avg_profit = np.mean(profit_20)
        profit_40 = mcs(x, n, units[2], price, unit_cost, disposal)
        avg_profit = np.mean(profit_40)
        profit_60 = mcs(x, n, units[3], price, unit_cost, disposal)
        avg_profit = np.mean(profit_60)
        avg_ls.append({'p10':np.mean(profit_10),
                       'p20':np.mean(profit_20),
                       'p40':np.mean(profit_40),
                       'p60':np.mean(profit_60)})
        y += 1
    mcs_p10, mcs_p20, mcs_p40, mcs_p60 = [], [], [], []
    for row in avg_ls:
        mcs_p10.append(row['p10'])
        mcs_p20.append(row['p20'])
        mcs_p40.append(row['p40'])
        mcs_p60.append(row['p60'])
    display(np.mean(mcs_p10))
    display(np.mean(mcs_p20))
    display(np.mean(mcs_p40))
    display(np.mean(mcs_p60))
