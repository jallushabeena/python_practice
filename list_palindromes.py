s = ["jkj", "malayalam", "dad", "mummy", "python", "aja"]
result = list(filter(lambda x: (x == "".join(reversed(x))), s)) 
print(result) 