# -*- coding: utf-8 -b*-

def detect_language(line):
    maxchar = max(line)
    if u'\u0c00' <= maxchar <= u'\u0c7f':
        return 'telugu'
    elif u'\u0900' <= maxchar <= u'\u097f':
        return 'hindi'
    return 'english'
inp=u'दवा'    
print inp
a=detect_language(inp)

print a