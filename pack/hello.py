def write():
    f = open("abcdef.txt", "wb")
    f.write("Hello Wordl")
    f.close()

if __name__ == "__main__":
    write()