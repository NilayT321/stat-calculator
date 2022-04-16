import scipy 
from scipy.stats import *
import statistics
import math

def mean_list (arr):
    sum = 0
    for x in arr:
        sum += x

    return sum / len(arr)

def stddev_list (arr, type = "samp"):
    avg = mean_list(arr)
    var_numerator = sum((x - avg) ** 2 for x in arr)

    if type == "samp":
        var = var_numerator / (len(arr) - 1)
    elif type == "pop":
        var = var_numerator / len(arr)
    else:
        return "ERROR: invalid value for argument \"type\". Should be either \"pop\" or \"samp\""

    return math.sqrt(var)

def one_sample_t_test (mu0, mean, std_dev, n, side, alpha = 0.05):
    # Calculate the standard error
    std_err = std_dev / math.sqrt(n)

    # Calculate degrees of freedom 
    df = n - 1

    # Calculate the t-statistic
    t_stat = (mean - mu0) / std_err

    # Get the side
    side_lower = side.casefold()

    # Calculate p-value, depends on the side
    if side_lower == 'left':
        pvalue = t.cdf(x = t_stat, df = df)
    elif side_lower == 'right':
        pvalue = 1 - t.cdf(x = t_stat, df = df)
    elif side_lower == 'two':
        pvalue = 2 * t.cdf(x = t_stat, df = df)
    else:
        print('ERROR: Invalid argument for parameter \"side\". Valid values are \"left\", \"right\", or \"two\""')

    # Calculate the confidence interval
    crit_value = t.ppf(alpha, df = df)
    moe = crit_value * std_err
    lower_value = mean - moe
    upper_value = mean + moe
    conf_level = (1 - alpha) * 100

    # Print output
    print("-----------------------------RESULTS OF ONE SAMPLE T-TEST-----------------------------")

    print("H0: mu =", mu0)

    if side_lower == 'left':
        print("H1: mu < ", mu0)
    elif side_lower == 'right':
        print("H1: mu >", mu0)
    else:
        print("H1: mu !=", mu0)

    print()
    print("Sample Mean:", mean)
    print("Sample Std. Dev:", std_dev)
    print("n:", n)
    print()

    print("T-stat:", t_stat)
    print("df:", df)
    print("P-value:", pvalue)
    print()
    
    print("Alpha:", alpha)
    print(f"{conf_level}% CI: ({lower_value}, {upper_value})")

def one_sample_t_test_from_data (arr, mu0, side, alpha = 0.05):
    mean = mean_list(arr)
    stddev = stddev_list(arr)
    n = len(arr)

    one_sample_t_test (mu0 = mu0, mean = mean, std_dev = stddev, n = n, side = side, alpha = alpha)

arr = [12, 24, 36, 48, 60]
one_sample_t_test_from_data(arr = arr, mu0 = 15, side = "left")
