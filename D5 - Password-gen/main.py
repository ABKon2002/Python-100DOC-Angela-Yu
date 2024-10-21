#Password Generator Project
import random
import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input("How many symbols would you like?: "))
nr_numbers = int(input("How many numbers would you like?: "))

def calculate_entropy(password, charset_size):
  return math.log2(charset_size) * len(password)

def calculate_brute_force_time(entropy, attempts_per_second=1e10):
  total_possible_passwords = 2 ** entropy
  seconds = total_possible_passwords / attempts_per_second
  return seconds

def display_time(seconds):
  years = seconds / (60 * 60 * 24 * 365)
  return years

def charset_size(password):
  size = 0
  if any(c.islower() for c in password):
      size += 26
  if any(c.isupper() for c in password):
      size += 26
  if any(c.isdigit() for c in password):
      size += 10
  if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password):
      size += 32
  return size

def password_strength(password):
  charset = charset_size(password)
  entropy = calculate_entropy(password, charset)
  time_to_crack = calculate_brute_force_time(entropy)
  years_to_crack = display_time(time_to_crack)

  return {
      "entropy": entropy,
      "time_to_crack_seconds": time_to_crack,
      "time_to_crack_years": years_to_crack
  }

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

def easyPassGen(aCount, sCount, nCount):
  password = ""
  for i in range(0, aCount):
    password += letters[random.randint(0, len(letters) - 1)]
  for i in range(0, sCount):
    password += symbols[random.randint(0, len(symbols) - 1)]
  for i in range(0, nCount):
    password += numbers[random.randint(0, len(numbers) - 1)]
  return password

# print(easyPassGen(nr_letters, nr_symbols, nr_numbers))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def hardPassGen(aCount, sCount, nCount):
  password = ""
  for i in range(0, aCount):
    password += letters[random.randint(0, len(letters) - 1)]
  for i in range(0, sCount):
    password += symbols[random.randint(0, len(symbols) - 1)]
  for i in range(0, nCount):
    password += numbers[random.randint(0, len(numbers) - 1)]
  passwordList = [char for char in password]
  random.shuffle(passwordList)
  password = "".join(passwordList)
  return password

genPassword = hardPassGen(nr_letters, nr_symbols, nr_numbers)
passwordStats = password_strength(genPassword)
print(f"Generated Password : {genPassword}")
print(f"This password will take {passwordStats['time_to_crack_seconds']} seconds to crack.")
print(f"i.e {passwordStats['time_to_crack_years']} years to crack.")
