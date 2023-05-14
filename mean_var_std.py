import numpy as np

def calculate(list):
    text = np.array(list)
    if len(list)!=9:
        raise ValueError('List must contain nine numbers.')
    else:
        a = text.reshape((3,3))
        mean_x = a.mean(axis=0)
        mean_y = a.mean(axis=1)
        mean = a.mean()
        var_x = a.var(axis=0)
        var_y = a.var(axis=1)
        var = a.var()
        std_x = a.std(axis=0)
        std_y = a.std(axis=1)
        std = a.std()
        max_x = a.max(axis=0)
        max_y = a.max(axis=1)
        max = a.max()
        min_x = a.min(axis=0)
        min_y = a.min(axis=1)
        min = a.min()
        sum_x = a.sum(axis=0)
        sum_y = a.sum(axis=1)
        sum = a.sum()


    calculations = {
        "mean": [mean_x.tolist(), mean_y.tolist(), mean.tolist()],
        "variance": [var_x.tolist(), var_y.tolist(), var.tolist()],
        "standard deviation": [std_x.tolist(), std_y.tolist(), std.tolist()],
        "max": [max_x.tolist(),max_y.tolist(), max.tolist()],
        "min": [min_x.tolist(),min_y.tolist(), min.tolist()],
        "sum": [sum_x.tolist(),sum_y.tolist(), sum.tolist()],
    }
    return calculations