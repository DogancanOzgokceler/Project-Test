# function definition:
def uniqueWolfs(wolf_list):

    # frequency array holds the number of repetitions for each wolf:
    frequency = [0, 0, 0, 0, 0]

    # iterate for all wolf in the list (by id):
    for wolf_id in wolf_list:

        # for the frequency index, 1 minus the id in the input list:
        frequency_index = wolf_id - 1

        # increase the repeat count of this id by 1:
        frequency[frequency_index] += 1

    # initialize the maximum frequency and the result id:
    max_freq = 0
    result_id = 0

    # iterate for all ids from 1 to 5:
    for wolf_id in range(1, 6):

        # for the frequency index, 1 minus the id in the input list:
        frequency_index = wolf_id - 1

        # get the frequency of the current wolf:
        wolf_freq = frequency[frequency_index]

        # compare this frequency value with the maximum frequency value so far:
        if wolf_freq > max_freq:

            # if this frequency value is greater than the maximum frequency value,
            # update the max_frequency value and the result_id
            max_freq = wolf_freq
            result_id = wolf_id

    # return the result_id as a result of the function
    return result_id


# examples:
print(uniqueWolfs([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
print(uniqueWolfs([3, 4, 4, 1, 4, 5, 2, 1]))
print(uniqueWolfs([2, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
print(uniqueWolfs([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 4, 4, 4]))
print(uniqueWolfs([1, 2, 3, 4, 1, 4, 3, 2, 1, 3, 4, 1, 2, 2]))
