inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

vorigeDiepte = int(lines[0])
aantalKeerDieper = 0
  
# Strips the newline character
for line in range(lines):
    diepte = int(line)

    diepte0 = int(lines[line])
    diepte3 = int(lines[line + 3])

    if diepte > vorigeDiepte and diepte:
      aantalKeerDieper = aantalKeerDieper + 1
    vorigeDiepte = diepte

    print(diepte0)
    print(diepte3)

#print(aantalKeerDieper)