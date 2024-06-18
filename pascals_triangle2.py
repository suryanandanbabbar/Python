def generate_pascals_triangle(n):
    if n > 0:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(row)

n = int(input("rows: "))
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)
