with open("style.css", "r") as file:
    file = file.read()

def getLines(file):
    lines = []
    line = []
    count = 0
    for char in file:
        line.append(char)
        if char == '\n':
            lines.append(''.join(line))
            line = []
            count += 1
    return lines
    
def getWidths(lines):
    for line in lines:
        if 'width' in line:
            print('width ', line[10])
    
lines = getLines(file)
getWidths(lines)
