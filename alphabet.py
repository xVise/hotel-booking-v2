with open('hotels.txt', 'r') as file:
    data = file.read()
    data = data.replace('------------------------------\n', '')
    lines = data.split('\n')
    lines = [line for line in lines if line.strip()]

    sorted_lines = sorted(lines, key=lambda x: x.split('"name": "')[1].split('"')[0])

with open('hotels.txt', 'w') as file:
    for line in sorted_lines:
        file.write(line + '\n')
        file.write('-' * 30 + '\n')