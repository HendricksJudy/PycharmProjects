#  集合推导式

'''
set1 = {1, 2, 3, 4}

set2 = {i<<1 for i in set1}
print(set2)

'''
set1 = {1, 2, 3, 4}

set2 = {i<<1 for i in set1 if i%2==0}



