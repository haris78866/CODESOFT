import random
import string 


def gen_password(length) :
    character=string.ascii_lowercase+string.ascii_uppercase+string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(character)for _ in range(length))
    return password


def main() :
    length=int(input('Enter the length for your password :'))

    if length<=0 :
        print('Enter the valaid password length :')
        return
    

    new_password=gen_password(length)
    print('Password :',new_password)

if __name__ == "__main__":            # to run dorectly the module 
    main()


