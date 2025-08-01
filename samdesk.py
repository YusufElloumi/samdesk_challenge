def is_safe_report(levels):
    # Check if all differences are between 1 and 3 (inclusive) and all increasing or all decreasing
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    if all(1 <= d <= 3 for d in diffs):
        return True  # strictly increasing
    if all(-3 <= d <= -1 for d in diffs):
        return True  # strictly decreasing
    return False

def process_input_file(filename):
    safe_count = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            levels = list(map(int, line.split()))
            if is_safe_report(levels):
                safe_count += 1
    print(f"Number of safe reports: {safe_count}")


if __name__ == "__main__":
    process_input_file("samsdesk_input.txt")