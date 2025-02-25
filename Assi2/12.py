# Write python function that prints out first n rows of pascal's triangle
def print_pascals_triangle(n):                             
    for row in range(n):
        number = 1
        for col in range(row + 1):
            print(number, end=" ")
            number = number * (row - col) // (col + 1)
        print()

# Example usage
n = 5
print_pascals_triangle(n)

'''Explanation:
The outer loop iterates over the rows of the triangle.
The inner loop calculates the values of each element in the current row.
The number is calculated using the formula from Pascal's Triangle, which is based on binomial coefficients.
end=" " ensures the values in each row are printed on the same line, and print() moves to the next row after each one.'''