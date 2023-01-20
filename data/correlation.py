import numpy
import scipy.stats as stats


def math_mean(arr):
    return float(stats.tmean(arr))


def covariation(arr_x, arr_y):  # function, that finds covariance of 2 arrays
    arr_x, arr_y = numpy.array(arr_x), numpy.array(arr_y)  # set 2 arrays to numpy array
    summ = 0
    mean_x, mean_y = math_mean(arr_x), math_mean(arr_y)  # find math mean of arrays
    for i in range(arr_x.size if arr_x.size < arr_y.size else arr_y.size):
        summ += (arr_y[i] - mean_y) * (arr_x[i] - mean_x)
    return summ / (arr_y.size - 1)


def Pearson_correlation_coefficient(arrX, arrY):  # this function calculate  Pearson coeff
    return covariation(arrX, arrY) / (covariation(arrX, arrX) ** 0.5 * covariation(arrY, arrY) ** 0.5)


if __name__ == '__main__':
    print(Pearson_correlation_coefficient([1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10, 12, 14]))
