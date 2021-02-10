import sys, math, random

# using global variable to put every permutation result in a list and then print it
random_perm = []

def generate_permutations(values, lenght):
    global random_perm
    if lenght == 0:
        # print(''.join(values))
        random_perm.append(''.join(values))
    else:
        for i in range(lenght):
            generate_permutations(values, lenght - 1)
            j = 0 if lenght % 2 == 0 else i
            values[j], values[lenght] = values[lenght], values[j]
        generate_permutations(values, lenght - 1)


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]
permutations_num = math.perm(len(word), len(word) - 1)
print("Possible permutations: " + str(permutations_num))

if permutations_num <= 20:
    generate_permutations(list(word), len(word) - 1)
    print(random_perm)
else:
    generate_permutations(list(word), len(word) - 1)
    print(random.choices(random_perm, k=20))
