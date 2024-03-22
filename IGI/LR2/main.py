import os
from geometric_lib import circle, square
AREA = int(os.environ["AREA"])
SIDE = int(os.environ["SIDE"])

print(f"circle AREA:{(circle.area(AREA))}\ncircle PERIMETER: {circle.perimeter(SIDE)}")
print(f"circle AREA:{(square.area(AREA))}\nsquare PERIMETER: {square.perimeter(SIDE)}")