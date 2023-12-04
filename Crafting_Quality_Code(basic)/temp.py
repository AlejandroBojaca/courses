import numpy as np

# List of portfolio values
step_profits = [
  0.0607, 0.2414, 0.1991, 0.4183, 0.5556, 0.7379, 1.0414, 1.0201, 0.8246, 1.5351,
  1.3840, 1.4119, 1.5566, 1.6747, 2.0342, 2.0770, 2.1456, 2.1110, 2.1651, 2.2550,
  2.1782, 2.2354, 1.9413, 1.9257, 2.0562, 1.9706, 1.8521, 1.9987, 2.0074, 2.0089,
  1.9267, 2.0014, 2.6842, 2.5040, 2.5268, 2.1230, 2.2844, 2.2910, 2.0063, 2.8616,
  2.8794, 2.9329, 2.9908, 2.7349, 2.8216, 2.5289
]

def draw_down_reducer(step_profits):
    result = {'maxDD': 0, 'allTimeHigh': 0}

    for cur_profit in step_profits:
        cur = {}
        
        cur['profit'] = cur_profit
        cur['allTimeHigh'] = max(result['allTimeHigh'], cur['profit'])

        next_max_dd = abs((cur_profit + 1) / (cur['allTimeHigh'] + 1) - 1)

        cur['maxDD'] = max(result['maxDD'], next_max_dd) if next_max_dd is not None else result['maxDD']

        result.update(cur)

    return result


result = draw_down_reducer(step_profits)
print(result)
