import os

if (not os.path.isdir('out/psalms')):
    os.makedirs('out/psalms')

with open('src/psalms1/Psalm1.txt', encoding='utf_8') as f:
    with open('out/psalms/psalm1.tex', 'w', encoding='utf_8') as o:
        for line in f:
            o.write(line)
            o.write('\n')
        orig = f.read()
        print(orig)
