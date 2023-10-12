def calculate_robot_position(n):
    x, y = 0, 0
    counter = 0
    size = 1
    
    while counter < n:
        
        for i in range(size):
            x -= 1
            counter += 1
            if counter == n:
                return x, y

        for i in range(size):
            y -= 1
            counter += 1
            if counter == n:
                return x, y
        size += 1

        for i in range(size):
            x += 1
            counter += 1
            if counter == n:
                return x, y

        for i in range(size):
            y += 1
            counter += 1
            if counter == n:
                return x, y
        size += 1

n = int(input())
if n == 0:
    print("0, 0")
else:
    x, y = calculate_robot_position(n)
    print((x, y))