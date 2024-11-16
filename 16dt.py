def generate_sequence(n):
    sequence = []
    current_num = 1
    while len(sequence) < n:
        sequence.extend([current_num] * current_num)
        current_num += 1
    print(*sequence[:n])
N = int(input())
generate_sequence(N)
