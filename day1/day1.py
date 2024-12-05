from functools import reduce

input_path:str = './input.txt'

def get_pairs() -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    current_pair: tuple[int, int]
    with open(input_path, "r") as f:
        for line in f.readlines():
            current_pair = (int(line.split()[0]), int(line.split()[1]))
            pairs.append((int(current_pair[0]), int(current_pair[1])))
    return pairs

def extract_ordered_lists(pairs: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    first_list: list[int] = list(map(lambda tup: tup[0], pairs))
    second_list: list[int] = list(map(lambda tup: tup[1], pairs))
    first_list.sort()
    second_list.sort()
    return (first_list, second_list)

def get_abs_distance(lists: tuple[list[int], list[int]]) -> int:
    (f_list, s_list) = lists
    pair_size = len(pairs)
    distance = 0
    for i in range(pair_size):
        distance += abs(f_list[i] - s_list[i])
    return distance

def similarity_dict_of(l: list[int]) -> dict[int, int]:
    similarity_dict: dict[int, int] = {}
    for num in l:
        if num in similarity_dict:
            similarity_dict[num] += 1
            continue
        similarity_dict[num] = 1
    return similarity_dict

def get_rank(element: int, similarity_dict: dict[int, int]) -> int:
    if element not in similarity_dict:
        return 0
    return element * similarity_dict[element]

def get_similarity_rank(lists: tuple[list[int], list[int]]) -> int:
    similarities: dict[int, int] = similarity_dict_of(lists[1]) 
    subproducts: list[int] = list(map(lambda element: get_rank(element, similarities), lists[0]))
    return reduce(lambda a, b: a+b, subproducts)

pairs = get_pairs()
(f_list, s_list) = extract_ordered_lists(pairs)

"""
Part 1
"""
print(f'Distance: {get_abs_distance((f_list, s_list))}')

"""
Part 2
"""
print(f'Similarity rank: {get_similarity_rank((f_list, s_list))}')
