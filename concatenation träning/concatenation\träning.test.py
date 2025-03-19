#......................................
# -- Concatenation --
#........................................

msg = "i love "
lang = "python"
print(msg + lang)

full = msg + " " + lang 
print(full)

a = "first \
    second \
        third"
a: str
b = "A \
    B \
        C"
        
print(a + b)
print(a + " " + b)
print(a + "\n" + b)
print("Hello" + 1) # Error den funkar inte 