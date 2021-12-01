def read_depth_measurements():
    output = []
    with open("input.txt") as f:
        for line in f:
            output.append(int(line))
    return output


def compare_with_previous(depth_list: list):
    count = 0
    previous_depth = depth_list[0]
    for i in depth_list[1:]:
        if i > previous_depth: count += 1
        previous_depth = i
    return count


def compare_via_sliding_window(depth_list: list):
    count = 0
    previous_window = depth_list[:3]
    previous_sum = sum(previous_window)
    for i, j in enumerate(depth_list[1:], start=1):
        previous_window[i%3] = j
        new_sum = sum(previous_window)
        if new_sum > previous_sum:
            count += 1
        previous_sum = new_sum
    return count


if __name__ == '__main__':
    input = read_depth_measurements()
    print(f"compare with previous value: {compare_with_previous(input)}")
    print(f"compare with sliding window: {compare_via_sliding_window(input)}")
