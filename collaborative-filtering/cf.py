import math
from functools import reduce

est_rating = [
    [None, None, None, 4, 4],
    [None, 5, None, None, 4],
    [None, None, None, 2, 3],
    [None, 2, 2, 3, 1],
    [None, 2, None, 1, None]
]

est_rating_mean = []

def cosSimilarity(x, y):
    a = 0
    for (counter, value) in enumerate(est_rating_mean[x]):
        if est_rating_mean[x][counter] is not None and est_rating_mean[y][counter] is not None:
            a += est_rating_mean[x][counter]*est_rating_mean[y][counter]
    b1 = math.sqrt(reduce(lambda p, q: p+q, list(map(lambda z: z**2, list(filter(None, est_rating_mean[x]))))))
    b2 = math.sqrt(reduce(lambda p, q: p+q, list(map(lambda z: z**2, list(filter(None, est_rating_mean[y]))))))
    return a/(b1*b2)

def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__, reverse=True)[1:]

for phone in est_rating:
    try:
        row_mean = sum(filter(None, phone))/float(len(list(filter(None, phone))))
        temp_phone = []
        for (j, rating) in enumerate(phone):
            if rating is not None:
                temp_phone.append(rating - row_mean)
            else:
                temp_phone.append(None)
        est_rating_mean.append(temp_phone)
    except ZeroDivisionError:
        est_rating_mean.append(phone)
    
target = 0
for target in range(len(est_rating)):
    cos_sim_list = []
    for i in range(len(est_rating)):
        try:
            cos_sim_list.append(round(cosSimilarity(target, i), 4))
        except:
            cos_sim_list.append(-1)

    for (index, r) in enumerate(est_rating[target]):
        if r is None:
            a = 0
            b = 0
            for rank in rank_simple(cos_sim_list)[:3]:
                if cos_sim_list[rank] > 0 and est_rating[rank][index] is not None:
                    a += est_rating[rank][index]*cos_sim_list[rank]
                    b += cos_sim_list[rank]
            try:
                est_rating[target][index] = round(a/b, 4)
            except ZeroDivisionError:
                est_rating[target][index] = None
    

print (est_rating)