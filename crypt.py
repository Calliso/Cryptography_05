from Shouldwork import Cipher

def main():
    c = Cipher('KwIatEKk')
    c.crypt('text.txt')
    c.decrypt('encrypted.txt')

if __name__ == "__main__":
    main()