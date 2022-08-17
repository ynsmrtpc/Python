import sys

# print(dir(sys))

# a = int(input("a:"))
# b = int(input("b:"))

# sys.exit() # programı sonlandırır


# c = int(input("c:"))

print("- - - - - - - - - - - - - - - ")

sys.stderr.write("bu bir hata mesajıdır!\n")
sys.stderr.flush()

sys.stdout.write("bu normal bir yazıdır!\n")

print("- - - - - - - - - - - - - - - ")

print(sys.argv)