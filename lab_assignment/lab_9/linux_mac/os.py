import os
os.mkdir("log")

if not os.path.isdir("log"):
    print("there isn't ", dir)
    os.mkdir("log")
