import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    pontos = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        pontos.append((x1, y1))
        
        if x1 == x2 and y1 == y2:
            break
            
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return pontos

x1, y1 = 2, 3
x2, y2 = 13, 8
pontos = bresenham(x1, y1, x2, y2)

x_vals, y_vals = zip(*pontos)
plt.plot(x_vals, y_vals, marker="o", color="b")
plt.title("Linha gerada pelo Algoritimo Bresenham")
plt.show()
