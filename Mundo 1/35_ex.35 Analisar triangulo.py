print("--==--Ex.35 Triangle analyzer --==--")
print("===----==="*12)
try:
	a = float(input("First segment: "))
	b = float(input("Second segment: "))
	c = float(input("Third segment: "))
	
except ValueError:
	print("\n[Erro)] Oops! You can only wrhite numbers and periods.")
	exit() 
	
if a + b > c and a + c > b and c + b > a:
	print("The segments above can form a triangle!")
else:
	print("The segments above can not form triangles!")