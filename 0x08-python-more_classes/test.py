def new(w,h): 
    rect = []
    for x in range(0, h):
        for y in range(0, w):
            rect.append('#')
        if y != 1:
            rect.append('\n')
    return ''.join(rect)

print(new(4,5))