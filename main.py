import enchant

d = enchant.Dict("es_ES")

def load_lines(filename):
    content = ''

    with open(filename) as f:
        content = f.read()

    lines = []

    table = content.split('\n')
    # if the last line is empty, remove/pop it
    if table[-1] == '':
        table.pop()

    width = len(table[0])
    height = len(table)

    # maintenant, on charge des lignes de différents manières
    # lignes horizontales
    for line_content in table:
        lines.append({
            'content': line_content,
            'type': 'horizontal_line'
        })

    # lignes verticales
    for i in range(0, width):
        # on assemble la ligne
        line_content = ''
        
        for line in table:
            line_content += line[i]
        
        lines.append({
            'content': line_content,
            'type': 'vertical_line'
        })

    # lignes diagonales: haut gauche à bas droit
    starting_x =  0
    starting_y = height

    def diagonal(x, y, vector_x, vector_y):
        line_content = ''

        # condition: not out of bound
        while (y >= 0 and y < height) and (x >= 0 and x < width):
            line_content += table[y][x]

            x += vector_x
            y += vector_y

        return line_content

    # on obtient la liste de tous les points qui sont aux côtés du carré

    side_points = []

    # tous les x, haut et bas
    for x in range(0, width):
        side_points.append((x, 0))
        side_points.append((x, height - 1))

    # tous les y, gauche(0) et droite(width-1)
    for y in range(0, height):
        side_points.append((0, y))
        side_points.append((width - 1, y))

    # on parcoure tous les types de diagonales à partir de tous les points de côté.
    for point in side_points:
        multiple_line_content = [
            diagonal(point[0], point[1], -1, -1),
            diagonal(point[0], point[1], -1, 1),
            diagonal(point[0], point[1], 1, -1),
            diagonal(point[0], point[1], 1, 1)
        ]

        for line_content in multiple_line_content:
            lines.append({
                'content': line_content,
                'type': 'diagonal'
            })

    # TODO: reversed equivalent of each line
    # reverse formula: elem[::-1]

    for i in range(0, len(lines)):
        lines.append({
            'content': lines[i]['content'][::-1],
            'type': 'reversed_' + lines[i]['type']
        })
        
    return lines


paridad_lines = load_lines('paridad.txt')
turismo_lines = load_lines('turismo.txt')
# print(paridad_lines)

# line = "fnenpsldstransgredir"

for line_with_metadata in turismo_lines:
    line = line_with_metadata['content']

    for i in range(0, len(line)):
        for j in range(i, len(line)):
            to_check = line[i:j + 1]
            if len(to_check) == 0 or len(to_check) < 4:
                continue
            
            if d.check(to_check):
                print("valid word: " + to_check + ' in ' + line_with_metadata['type'])
