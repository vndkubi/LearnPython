#Sort str[]

string =  input("Input your string and between two string with ',': ")
arrString = [s for s in string.split(",")]
arrString.sort()
print(', '.join(arrString))