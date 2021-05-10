import random
import string


def main(size):
    chars = string.ascii_letters + string.digits + '!@#$ç%&*-+'
    rand = random.SystemRandom()
    print(''.join(rand.choice(chars) for i in range(size)))


if __name__ == '__main__':
    i = 0
    size = input('White size for password: ')
    main(int(size))
    while i != 1:
        response = input('Want another password? (Y/N) ')
        if response.upper() == 'Y':
            main(int(size))
        else:
            i = 1
