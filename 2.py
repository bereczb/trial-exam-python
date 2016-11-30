# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def counter(name_of_file):

    try:
        f = open(name_of_file, 'r')
        text_list = f.readlines()
        f.close()
    except:
        return 0

    letter_a_in_file = 0

    for i in range(len(text_list)):
        for j in range(len(text_list[i])):
            if text_list[i][j] == 'a':
                letter_a_in_file += 1

    return letter_a_in_file

    # letter_a_in_filename = 0
    #
    # for i in range(len(name_of_file)):
    #     if name_of_file[i] == 'a':
    #         letter_a_in_filename += 1
    #
    # return letter_a_in_filename


print(counter('test_a.txt'))
