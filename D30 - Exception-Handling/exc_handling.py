
try:    # A block of code that might cause an error (exception)
    # File not found error
    data = open('a_file.txt', 'r')     # Notice that this code block will stop its execution here itself.
    # Key error
    dict = {'key': 'value'}
    print(dict['not_a_key'])
    # Index error
    nums = [1,2,3,4]
    print(nums[4])

except FileNotFoundError:   # blocks of code to handle the error based on their type
    print("That file doesn't exist.")
except KeyError as error:
    print(f"Key {error} doesn't exist.")
except IndexError:
    print("You tried to access an index that doesn't exist.")

else:    # blocks of code to execute if there is no error
    print("Code ran successfully.")

finally:    # blocks of code to execute no matter what
    print("Code ran no matter what.")

print("\n**************************************\n")

# Raising our own errors
height = int(input("Enter your height in meters (m): "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
