def my_function(list):
    result = {}

    unique_values = sorted(set(list))

    for i in unique_values:
        count =0
        for j in list:
            if j<=i:
                count+=1
        result[i] = (count/len(list)) * 100
    return result

print(my_function([1,2,3,4,5,6,7,8,9]))
