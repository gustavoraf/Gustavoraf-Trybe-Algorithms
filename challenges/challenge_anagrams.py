def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())
    merge_sort(first_string_list)
    merge_sort(second_string_list)
    return first_string_list == second_string_list


def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge(list, start, mid, end)


def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    left_idx, right_idx = 0, 0
    for main_idx in range(start, end):
        if left_idx >= len(left):
            list[main_idx] = right[right_idx]
            right_idx += 1
        elif right_idx >= len(right):
            list[main_idx] = left[left_idx]
            left_idx += 1
        elif left[left_idx] < right[right_idx]:
            list[main_idx] = left[left_idx]
            left_idx += 1
        else:
            list[main_idx] = right[right_idx]
            right_idx += 1
