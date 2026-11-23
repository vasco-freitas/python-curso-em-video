lados = []
lados.append(float(input("First segment: ")))
lados.append(float(input("Second segment: ")))
lados.append(float(input("Third segment: ")))

#small = min(fir, sec, thi)
#big = max(fir, sec, thi)
#med = (big + sec + small) - big - small
organizado = sorted(lados)
small, med, big = organizado

if big >= (small + med):
    print("\nThe numbers do not form any triangle.")
else:   
    if small == med == big:
        print("\nThe segments above can form an equilateral triangle.")
    elif small == med or med == big or big == small:
        print("\nThe segments above can form an isosceles triangle.")
    else:
        print("\nThe segments above can form an scalene triangle.")