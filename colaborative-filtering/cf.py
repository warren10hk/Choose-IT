import math

phones = [
    [None, 3, 5, 2, 4],
    [None, 5, None, None, 4],
    [2, None, None, 2, 3],
    [2, 2, 2, 3, 1],
    [1, 2, None, 1, None]
]

phones_mean = []

def cosSimilarity(x, y):
    a = 0
    for (counter, value) in enumerate(phones_mean[x]):
        if phones_mean[x][counter] is not None and phones_mean[y][counter] is not None:
            a += phones_mean[x][counter]*phones_mean[y][counter]
    b1 = math.sqrt(reduce(lambda p, q: p+q, map(lambda z: z**2, filter(None, phones_mean[x]))))
    b2 = math.sqrt(reduce(lambda p, q: p+q, map(lambda z: z**2, filter(None, phones_mean[y]))))
    return a/(b1*b2)

def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__, reverse=True)[1:]

for phone in phones:
    row_mean = sum(filter(None, phone))/float(len(filter(None, phone)))
    temp_phone = []
    for (j, rating) in enumerate(phone):
        if rating is not None:
            temp_phone.append(rating - row_mean)
        else:
            temp_phone.append(None)
    phones_mean.append(temp_phone)

target = 0
for target in range(len(phones)):
    cos_sim_list = []
    for i in range(len(phones)):
        cos_sim_list.append(round(cosSimilarity(target, i), 4))

    for (index, r) in enumerate(phones[target]):
        if r is None:
            a = 0
            b = 0
            for rank in rank_simple(cos_sim_list)[:3]:
                if cos_sim_list[rank] > 0 and phones[rank][index] is not None:
                    a += phones[rank][index]*cos_sim_list[rank]
                    b += cos_sim_list[rank]
                    print a, b
            phones[target][index] = round(a/b, 4)

print phones