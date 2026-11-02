numbers = list(map(int, input().split()))
write_index = 0
for read_index in range(len(numbers)):
    if numbers[read_index] != 0:
        numbers[write_index], numbers[read_index] = numbers[read_index], numbers[write_index]
        write_index += 1
print(*numbers)