# \r\n -> CRLF = QUEBRA DE LINHA no windows
# \n -> LF     = QUEBRA DE LINHA no linux

print(12, 34, 1011, sep="-", end="\r\n") # Ctrl + c depois Ctrl + d, copia a linha para baixo
print(56, 78, sep="-", end="##\n")
print(9, 10, sep="-", end="\n##")