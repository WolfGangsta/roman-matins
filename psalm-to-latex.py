import os

if (not os.path.isdir('out/psalms')):
    os.makedirs('out/psalms')

with open('src/psalms1/Psalm1.txt', encoding='utf_8') as f:
    with open('out/psalms/psalm1.tex', 'w', encoding='utf_8') as o:
        lines = f.readlines()
        counter = 0
        for line in lines:
            words = line.split(' ')
            words = words[1:]

            if counter == 0:
                # First line: first word has lettrine
                words[0] = '\\lettrine[lines=3]{{\\color{red} ' + words[0][0] + '}}{' + words[0][1:] + '}'
            elif counter % 2 == 1:
                # Second, fourth, ... lines: first letter is blue
                words[0] = '{\\color{blue}\\textbf {' + words[0][0] + '}}' + words[0][1:]
            else:
                # Third, fifth, ... lines: first letter is red
                words[0] = '{\\color{red}\\textbf {' + words[0][0] + '}}' + words[0][1:]

            for wordIdx in range(1, len(words)):
                # Color asterisks red
                if words[wordIdx] == '*':
                    words[wordIdx] = '{\\color{red} *}'
                
                # TODO: Add daggers

            line = ' '.join(words)

            # Add paragraph end marker to final line
            if counter == len(lines) - 1:
                line += '\\par'

            o.write(line)
            counter += 1
        orig = f.read()
        print(orig)
