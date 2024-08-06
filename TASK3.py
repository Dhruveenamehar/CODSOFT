import random
import string

def generate_password(length, use_uppercase, use_digits, use_punctuation):
  
    character_set = string.ascii_lowercase 
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_digits:
        character_set += string.digits
    if use_punctuation:
        character_set += string.punctuation

   
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    return password

def get_user_preferences():
   
    try:
       
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return None, None, None, None

        
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_punctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'

        return length, use_uppercase, use_digits, use_punctuation

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None, None, None, None

def main():
    
    length, use_uppercase, use_digits, use_punctuation = get_user_preferences()

    if length is not None:
        
        password = generate_password(length, use_uppercase, use_digits, use_punctuation)
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()