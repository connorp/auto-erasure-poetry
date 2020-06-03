#!/usr/bin/env python3
# for some text, put it in HTML with styled spans
# could be restructured to read from stdin

startspan = '<span style="color:'
midspan = '">'
endspan = '</span>'

outtext = ['<p>']

with open('poem.txt', 'r') as infile:
    for line in infile:
        words = line.split()
        if len(words) == 0:
            outtext.append('</p>\n\n<p>')
            continue
        newstring = []
        for word in words:
            if len(word) <= 5:
                newstring.append(word)
            else:
                color = 'red'
                newstring.append(startspan+color+midspan+word+endspan)

        outtext.append(' '.join(newstring) + '<br/>\n')

outtext.append('</p>')

with open('poem.html', 'w') as outfile:
    outfile.writelines(outtext)
