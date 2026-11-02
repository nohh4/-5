digits = input().strip()
candidates = [int(digits[:i] + digits[i + 1:] or "0") for i in range(len(digits))]
print(max(candidates))