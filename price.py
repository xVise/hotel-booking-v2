with open('hotels.txt', 'r') as file:
    data = file.read()
    data = data.replace('------------------------------\n', '')
    lines = data.split('\n')
    lines = [line for line in lines if line.strip()]

    lines.sort()

with open('hotels.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
        file.write('-' * 30 + '\n')