import numpy as np


def check_pareto(arr):
    """
    Check pareto optimality among array of vectors.
    One vector is pareto optimal
    iff
    there do not exist a vector whose all elements are greater or equal than the vector's elements elementwise
    (At least one strict inequality needed)
    
    :param arr:
    :return: 
    """
    shape = np.shape(arr)

    # optimization needed
    for i in range(shape[0]):
        target_vector = arr[i]
        geq_arr = (target_vector <= arr)
        g_arr = (target_vector < arr)

        agg_geq_arr = np.prod(geq_arr, axis=1)  # check elementwise >=
        agg_g_arr = np.sum(g_arr, axis=1)  # check at least one element >
        result_arr = np.logical_and(agg_geq_arr, agg_g_arr)
        result = np.sum(result_arr)
        if result > 0:
            print(f'{target_vector} is not pareto optimal')
        else:
            print(f'{target_vector} is pareto optimal')


if __name__ == '__main__':
    arr = np.array([
        [5, 5],
        [1, 10],
        [10, 1],
        [3, 3]
    ])

    check_pareto(arr)