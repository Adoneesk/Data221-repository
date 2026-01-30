def convert_list_of_strings_to_dictionary(user_list):
    new_dictionary = {}
    for i in user_list:
        if len(i)%2 ==0:
            parity = "even"
        else:
            parity = "odd"
            new_dictionary[i] = {"length":len(i), "parity": parity}
    return new_dictionary
#

