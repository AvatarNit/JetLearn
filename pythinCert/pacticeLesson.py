class AdvancedNumber:
    def __init__(self,value):
        self.value = value
    
    def __add__(self,other):
        return AdvancedNumber(self.value + other.value)
    def __sub__(self,other):
        return AdvancedNumber(self.value - other.value)
    def __mul__(self,other):
        return AdvancedNumber(self.value * other.value)
    def __truediv__(self,other):
        return AdvancedNumber(self.value / other.value)
    

    def __and__(self,other):
        return AdvancedNumber(self.value & other.value)
    def __or__(self,other):
        return AdvancedNumber(self.value | other.value)
    def __xor__(self,other):
        return AdvancedNumber(self.value ^ other.value)
    def __invert__(self):
        return AdvancedNumber(~self.value)
    
    def __eq__(self,other):
        return self.value == other.value
    def __ne__(self,other):
        return self.value != other.value
    def __lt__(self,other):
        return self.value < other.value
    def __le__(self,other):
        return self.value <= other.value
    def __gt__(self,other):
        return self.value > other.value
    def __ge__(self,other):
        return self.value >= other.value
    
    def __bool__(self):
        return self.value != 0
    
    def __str__(self):
        return f"AdvancedNumber({self.value})"

num1 = AdvancedNumber(10)
num2 = AdvancedNumber(5)
num3 = AdvancedNumber(0)

print("Arithmetic Operations:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print("\nBitwise Operations:")
print(f"{num1} & {num2} = {num1 & num2}")
print(f"{num1} | {num2} = {num1 | num2}")
print(f"{num1} ^ {num2} = {num1 ^ num2}")
print(f"~{num1} = {~num1}")
print("\nComparison Operations:")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print("\nLogical Operations:")
print(f"bool({num1}) = {bool(num1)}")
print(f"bool({num3}) = {bool(num3)}")
print("\nCustom String Representation:")
print(str(num1))
print(str(num2))