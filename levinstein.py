def levenstein_dist(str1, str2):
    dist = [i for i in range((len(str1) + 1))]

    for idx2 in range(1, len(str2)+1):
        next_dist = [0] * (len(str1) + 1)
        next_dist[0] = idx2
        for idx1 in range(1, len(str1)+1):
            if str1[idx1-1] == str2[idx2-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            next_dist[idx1] = min(dist[idx1] + 1, next_dist[idx1-1] + 1, dist[idx1-1] + substitution_cost)
        dist = next_dist
    return dist


print(levenstein_dist("sitten", "sitting"))

