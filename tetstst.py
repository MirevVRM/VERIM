# plants_filled = [[1.0, 1.0, 2.0, 1.0, 1.01, 1.01], [39.0, 1.0, 311.0, 310.0, 2.34, 2.34], [150.0, 1.0, 3001.0, 3000.0, 10.0, 10.0], [1.0, 52.847, 3052.847, 3000.0, 10.0, 528.47], [112.0, 52.847, 468.847, 416.0, 7.83, 413.792], [150.0, 52.847, 53.847, 1.0, 1.01, 53.375], [1.0, 134.031, 1154.031, 1020.0, 4.46, 597.778], [97.0, 134.031, 159.031, 25.0, 7.22, 967.704], [150.0, 134.031, 2647.031, 2513.0, 2.08, 278.784]]
# parameters_RB = [12, 2525.44, 24.256]
# sorted_list_plants = [[1, 1.0, 1.01, 2.0, 1.0, 1.01, 1.01], [6, 150.0, 53.375, 53.847, 1.0, 1.01, 53.375], [8, 97.0, 967.704, 159.031, 25.0, 7.22, 967.704], [2, 39.0, 2.34, 311.0, 310.0, 2.34, 2.34], [5, 112.0, 413.792, 468.847, 416.0, 7.83, 413.792], [7, 1.0, 597.778, 1154.031, 1020.0, 4.46, 597.778], [9, 150.0, 278.784, 2647.031, 2513.0, 2.08, 278.784], [3, 150.0, 10.0, 3001.0, 3000.0, 10.0, 10.0], [4, 1.0, 528.47, 3052.847, 3000.0, 10.0, 528.47]]

# list_1 = [[1, 2.45], [2, 25.445], [3, 342.45], [4, 223.645]]



# import numpy as np
#
# # Creating a 1D array
# a1 = np.array([1, 2, 3])
# print("1D array:\n", a1)
#
# # Creating a 2D array
# a2 = np.array([[1, 2, 3], [4, 5, 6]])
# print("\n2D array:\n", a2)
#
#
#
# # Creating a 2x3 array of zeros
# z = np.zeros((2, 3))
# print("Array of zeros:\n", z)
#
#
#
# # Creating a 3x2 array of ones
# o = np.ones((3, 2))
# print("Array of ones:\n", o)
#
#
#
# # Creating an array of numbers from 0 to 9
# ar = np.arange(10)
# print("Array from 0 to 9:\n", ar)
#
# # Creating an array from 10 to 19
# ar2 = np.arange(10, 20)
# print("\nArray from 10 to 19:\n", ar2)
#
# ar2 = np.arange(0, 6, 5)
# print("\nArray from 10 to 19:\n", ar2)
#
# # Creating an array of 5 numbers, evenly spaced between 0 and 1
# l = np.linspace(0, 6, 5)
# print("Array with linspace:\n", l)


# 1. Basic Indexing
# Accessing and modifying elements in an array using their index.

# import numpy as np
#
# # Creating a 2D array
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# # Accessing an element (row 1, column 2)
# print("Element at row 1, column 2:", arr[1, 2])
#
# # Modifying an element
# arr[1, 2] = 10
# print("\nModified array:\n", arr)
#
#
#
#
# # 2. Slicing
# # Extracting a portion of an array.
#
# # Slicing a subset of the array (first two rows, columns 1 and 2)
# subset = arr[:2, 1:3]
# print("Sliced array:\n", subset)
#
# n, m, z, p = 1, 3, 1, 3
# subset = arr[n:m, z:p]
# print("Sliced array:\n", subset)




# # 3. Fancy Indexing
# # Using arrays of indices to access multiple elements.
#
# # Creating an array
# arr2 = np.array([[10, 20, 30, 40, 50], [11, 22, 33, 44, 55]])
#
# # Accessing multiple elements (at positions 1, 3, and 4)
# fancy_subset = arr2[[1, 3, 4]]
# print("Fancy indexing result:\n", fancy_subset)




# # 4. Boolean Indexing
# # Selecting elements using conditionals.
#
# # Creating an array
# arr3 = np.array([1, 2, 3, 4, 5, 6])
#
# # Boolean indexing
# bool_index = arr3 > 3
# print("Boolean index:\n", bool_index)
#
# # Using the boolean index to select elements
# selected_elements = arr3[bool_index]
# print("Selected elements:\n", selected_elements)
#
#
# bool_index = np.array([True, True, False, False, True, True])
# selected_elements = arr3[bool_index]
# print("Selected elements:\n", selected_elements)
#
# arr4 = np.array([[1, 2, 3, 4, 5, 6], [11, 22, 33, 44, 55, 66]])
# bool_index = arr4 > 4
# print(bool_index)
# selected_elements = arr4[bool_index]
# print("Selected elements:\n", selected_elements)


# Reshaping Arrays
# Changing the shape of an array without altering its data.

# import numpy as np
#
# # Creating a 1D array
# arr = np.arange(6)
# print("Original array:\n", arr)

# # Reshaping it to a 2x3 array
# reshaped_arr = arr.reshape((2, 3))
# print("\nReshaped array (2x3):\n", reshaped_arr)
#
# # Reshaping it to a 3x3 array
# reshaped_arr = arr.reshape((3, 2))
# print("\nReshaped array (3x2):\n", reshaped_arr)
#
# reshaped_arr_2 = reshaped_arr.reshape(2, 3)
# print("\nReshaped array111 (2x3):\n", reshaped_arr_2)


# # Joining Arrays
# # Using np.concatenate to join two or more arrays.
#
# # Creating two arrays
# arr1 = np.array([[1, 2], [3, 4]])
# print("Arr1:", arr1, " ", arr1.shape, " ", arr1.ndim)
#
# arr2 = np.array([[5, 6]])
# print("Arr2:", arr2, " ", arr2.shape, " ", arr2.ndim)
#
# # Concatenating along the first axis (rows)
# concatenated_arr = np.concatenate([arr1, arr2], axis=0)
# print("Concatenated along rows:\n", concatenated_arr)
#
# # Concatenating along the second axis (columns) requires same number of rows
# arr3 = np.array([[7, 8]])
# print("Arr3:", arr3, " ", arr3.shape, " ", arr3.ndim)
# arr4 = arr3.T # .T is transpose
# print("Arr4.T:", arr4, " ", arr4.shape, " ", arr4.ndim)
#
# concatenated_arr2 = np.concatenate([arr1, arr4], axis=1)
# print("\nConcatenated along columns 1:\n", concatenated_arr2)
#
# concatenated_arr3 = np.concatenate([arr1, arr1], axis=None)
# print("\nConcatenated along columns 2:\n", concatenated_arr3)
#
# concatenated_arr3 = np.concatenate([arr1, arr1.T], axis=None)
# print("\nConcatenated along columns 2:\n", concatenated_arr3)


# # Splitting Arrays
# # Dividing arrays into multiple sub-arrays using np.split.
#
# # Splitting an array into 3 equal parts
# arr_to_split = np.array([1, 2, 3, 4, 5, 6])
# split_arr = np.split(arr_to_split, 2)
# print("Split array into 3 parts:\n", split_arr)
#
# print(type(arr_to_split))
# print(type(split_arr))
# print(type(split_arr[0]))
#
#
# # Adding/Removing Elements
# # Using np.append, np.delete, and np.insert.
#
# # Appending an element to the array
# appended_arr = np.append(arr, [7])
# print("Appended array:\n", appended_arr)
#
# # Deleting an element at index 2
# deleted_arr = np.delete(arr, 2)
# print("\nArray with element at index 2 deleted:\n", deleted_arr)
#
# # Inserting an element at index 1
# inserted_arr = np.insert(arr, 1, 10)
# print("\nArray with 10 inserted at index 1:\n", inserted_arr)
#
#
# x = np.arange(8).reshape(2, 4)
# idx = (1, 3)
# puppy = np.insert(x, idx, 999, axis=1)
#
# print(puppy)



# # NumPy Data Types (dtype)
# # NumPy offers various data types, and choosing the right one can significantly impact memory usage and computational efficiency. Here's how you can work with them:
# # Example 1: Specifying Data Type at Array Creation
#
# import numpy as np
#
# # Creating an array with a specific data type
# int_array = np.array([1, 2, 3, 4], dtype=np.int32)
# print("Integer Array:", int_array)
# print("Data type:", int_array.dtype)
#
# float_array = np.array([1, 2, 3, 4], dtype=np.float64)
# print("\nFloat Array:", float_array)
# print("Data type:", float_array.dtype)
#
#
# # In this example, we create arrays with specific data types: int32 and float64. Using dtype, you can control the precision and range of your data.
# # Example 2: Changing the Data Type of an Existing Array
#
# # Changing the data type of the array
# new_dtype_array = int_array.astype(np.float64)
# print("Array with Changed Data Type:", new_dtype_array)
# print("New Data type:", new_dtype_array.dtype)
#
# float_array = np.array([1.11, 2.25, 3.49, 4.82], dtype=np.float64)
# new_dtype_array_2 = float_array.astype(np.int32)
# print("Array with Changed Data Type 2:", new_dtype_array_2)
# print("New Data type 2:", new_dtype_array_2.dtype)
#
#
# # Here, astype is used to change the data type of an existing array. This can be important when you need to perform operations that require a certain type of data.
# # Example 3: Understanding Memory Usage
#
# # Comparing memory usage
# print("Memory size of int_array (int32):", int_array.nbytes, "bytes")
# print("Memory size of float_array (float64):", float_array.nbytes, "bytes")
#
#
# # The nbytes attribute shows the total memory consumed by the array. Smaller data types like int32 consume less memory compared to larger data types like float64.



# # Array Mathematics and Element-wise Operations
# # Basic Arithmetic Operations
# # Performing addition, subtraction, multiplication, and division on arrays.
#
# import numpy as np
#
# # Creating two arrays
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
# # Addition
# addition = a + b
# print("Addition:\n", addition)
#
# # Subtraction
# subtraction = a - b
# print("\nSubtraction:\n", subtraction)
#
# # Multiplication
# multiplication = a * b
# print("\nMultiplication:\n", multiplication)
#
# # Division
# division = a / b
# print("\nDivision:\n", division)
#
#
#
# # Trigonometric, Exponential, and Logarithmic Functions
# # NumPy provides a wide range of mathematical functions that can be performed element-wise on arrays.
#
# # Trigonometric function - Sine
# sine = np.sin(a)
# print("Sine:\n", sine)
#
# # Exponential function
# exp = np.exp(a)
# print("\nExponential:\n", exp)
#
# # Logarithmic function
# log = np.log(a)
# print("\nLogarithm:\n", log)
#
#
#
# # Broadcasting
# # Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. The smaller array is "broadcast" across the larger array so that they have compatible shapes.
#
# # Broadcasting with a scalar
# scalar = 10
# broadcast_with_scalar = a + scalar
# print("Broadcasting with scalar:\n", broadcast_with_scalar)
#
# # Broadcasting with different shapes
# c = np.array([[1], [2], [3]])
# broadcast_with_different_shapes = a * c
# print("\nBroadcasting with different shapes:\n", broadcast_with_different_shapes)
#
#
# # In the broadcasting example, a + scalar adds the scalar to each element in array a, while a + c demonstrates how an array with shape (3, 1) can be added to an array with shape (3,) to produce a (3, 3) array. This showcases NumPy's flexibility in handling arrays of different shapes for element-wise operations.



# 6. Advanced Operations
# Linear Algebra
# Using np.linalg for matrix operations.

# import numpy as np
#
# # Matrix multiplication
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# matrix_product = np.dot(A, B)
# print("Matrix Product:\n", matrix_product)
#
# # Determinant
# determinant = np.linalg.det(A)
# print("\nDeterminant of A:", determinant)
#
# # Eigenvalues
# eigenvalues, eigenvectors = np.linalg.eig(A)
# print("\nEigenvalues of A:", eigenvalues)
# print("Eigenvectors of A:\n", eigenvectors)
#
#
#
# # Statistics
# # Using NumPy's statistical functions.
#
# # Creating an array
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# # Mean
# mean = np.mean(data)
# print("Mean:", mean)
#
# # Median
# median = np.median(data)
# print("Median:", median)
#
# # Standard Deviation
# std_dev = np.std(data)
# print("Standard Deviation:", std_dev)
#
#
#
# # Random Module
# # Generating random numbers and samples with np.random.
#
#
# # Generating a single random number between 0 and 1
# random_number = np.random.rand()
# print("Random Number:", random_number)
#
# # Generating a random integer within a specified range
# random_integer = np.random.randint(0, 100)
# print("\nRandom Integer between 0 and 100:", random_integer)
#
# # Creating a random array
# random_array = np.random.rand(5)
# print("\nRandom Array:", random_array)
#
# # Random sampling from a normal distribution
# normal_sample = np.random.normal(0, 1, 5)  # mean = 0, std = 1, sample size = 5
# print("\nRandom Sample from Normal Distribution:", normal_sample)

number_digits_after_the_comma = 7

rounded_number = round(3.14559, number_digits_after_the_comma)
print(rounded_number)

x = 12 * 4 / 8.5
print(x)

number_digits_after_the_comma = 4

x = round(x, number_digits_after_the_comma)
print(x)

print(12.235 * 4.6347)

number_digits_after_the_comma = 4
ostatok = 134.0111
plant_1 = 1526.124
stream_1 = 3462.2347
table_3 = 2141.361
stream = 325.123

required_volume_flow_rate_from_table_3 = round(ostatok * (plant_1 - stream_1) / (table_3 - stream), number_digits_after_the_comma)
print(required_volume_flow_rate_from_table_3)

required_volume_flow_rate_from_table_3 = ostatok * (plant_1 - stream_1) / (table_3 - stream)
required_volume_flow_rate_from_table_3 = round(required_volume_flow_rate_from_table_3, number_digits_after_the_comma)
print(required_volume_flow_rate_from_table_3)

















