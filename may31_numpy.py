import numpy as np
"""
#create an ndarray
arr1= np.array([1,1,3,4,5])
print(arr1)

# create an array with a given range
arr2= np.arange(1,50,5)
print(arr2)

# create an array with values having equal gaps
arr3= np.linspace(2,4,num=5)
print(arr3)

# copy the the ndarray into another array
arr2= np.arange(1,50,5)
arr4= arr2.copy()
print(arr4)


# viewing the ndarray with another array
arr2= np.arange(1,50,5)
arr5= arr2.view()
print(arr5)

# reshape the array (change its dimensions)
arr6 = np.array([(1,2,3),(3,4,5)])
print("Before reshape: ",arr6)
arr7= arr6.reshape(3,2)
print("After reshape : ",arr7)

# to join arrays
arr8= np.array([(1,2,4),(4,5,6)])
arr9= np.array([(10,4,12),(20,21,22)])
arr10= np.concatenate((arr8,arr9),axis=1)
print(arr10)

# to find an item in array
arr1= np.array([1,1,3,4,5])
item= np.where(arr1==1)
print("Item found in arr1 at: ",item)
"""

arr= np.array([(1,2,3,4),(3,4,4,6)])
arr1= arr.reshape(-1,1)
print(arr1)
