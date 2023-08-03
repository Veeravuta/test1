#1. Print all Pairs which make sum N for the given list.
#e,g: l = [4, 3, 6, 8, 2, 9, 7,  5]
#N = 10,
#It should print (4, 6), (8, 2), (3, 7)
l = [4, 3, 6, 8, 2, 9, 7, 5]
N = 10

result = find_pairs_with_sum(l, N)
print(result)