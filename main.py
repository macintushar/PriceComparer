from amazon import *
from flipkart import *
import time
import amazon
import flipkart

print("Please note that you HAVE to mention the exact product details (Storage, Processor, etc.")
print()
time.sleep(5)
userName = input("Enter the name of the product: ")
userPrice = input("Enter the price of the product: ")
amz_pr(userName)
flip_prod(userName)
print("The price you entered is:",userPrice)
print()
print("thanks for testing!")