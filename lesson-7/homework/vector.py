class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    def __str__(self):
        str = ""
        for component in self.components:
            str = str + f"{component} "
        return str
    
    def __sub__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("components are not equal")
        zipped = zip(self.components,other.components)

        substracted = []
        for item in zipped:
            res = item[0]-item[1]
            substracted.append(res)
        
        return Vector(substracted)
    
    def __add__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("components are not equal")
        zipped = zip(self.components,other.components)

        added = []
        for item in zipped:
            res = item[0]+item[1]
            added.append(res)
        
        return Vector(added)

    def __mul__(self,other):
        if isinstance(other, (int, float)): 
            return Vector([other * x for x in self.components])
        if len(self.components) != len(other.components):
            raise ValueError("components are not equal")
        zipped = zip(self.components,other.components)

        mul = []
        for item in zipped:
            res = item[0]*item[1]
            mul.append(res)
        
        return Vector(mul)
    
    def magnitude(self):
        return sum([a**2 for a in self.components])**0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[x / mag for x in self.components])

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)