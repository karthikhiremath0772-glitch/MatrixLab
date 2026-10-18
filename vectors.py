# Vector scaler operations 
import numpy as np

s=5
v=np.array([1, 2, 3])
print("1. Vector scaler operations")
#Scaler addition
add_result=s+v
print(f"{s}+{v}={add_result}")

#Scaler substraction
sub_result=s-v
print(f"{s}-{v}={sub_result}")

#Scaler multiplication
mul_result=s*v
print(f"{s}*{v}={mul_result}")

#Scaler divivion
div_result=s/v
print(f"{s}/{v}={div_result}")


print("2. Vector Vector operations")
u=np.array([1, 2, 3])
v=np.array([4, 5, 6])

#Vector addition 
add_res=u+v
print(f"{u}+{v}={add_res}")

#Vector Substraction
sub_res=u-v
print(f"{u}-{v}={sub_res}")

#Vector Multiplication
mul_res=u*v
print(f"{u}*{v}={mul_res}")

#Vector Division
div_res=u/v
print(f"{u}/{v}={div_res}")


#Dot product of two vectors
dot_product=np.dot(u, v)
print(f"Dot product of {u} and {v} is {dot_product}")
