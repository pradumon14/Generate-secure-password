import random
import string

def generate_password(length=16):
    """Generate a secure password with the specified lengt>
    # Get a random selection of upper and lower case lette>
    characters = string.ascii_letters + string.digits + st>    # Use random.sample to choose `length` random elements>
    password = ''.join(random.sample(characters, length))      return password

# Generate a password with the default length of 16 charac>password = generate_password()
print("Here is the password: ",password)
