immutable_var = True, 3, "str", [1,2], 4.6
print(immutable_var)

#immutable_var[1] = False
#менять значения элементов кортежа нельзя

mutable_list =  [True, 3, "str", [1,2], 4.6]
mutable_list[0] = False
print(mutable_list)