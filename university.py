from copy import copy

departments = {'Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics'}

def load_data():
    list = []
    with open('applicants.txt') as file:
        for ln in file:
            list.append(ln.split())
    return list

def sort_gpa():
    apps.sort(key=lambda x: (-float(x[2]), x[0], x[1]))

# d - department, k = 1..3 - rank
def choise_by_rank(d, k):
    n1 = n - len(map_by_dep[d])
    app_d = [a for m, a in enumerate(filter(lambda x: x[k + 2] == d, apps)) if m < n1]
    map_by_dep[d] += app_d
    for a in app_d:
        apps.remove(a)
    if len(map_by_dep[d]) == n:
        dep_to_do.remove(d)
    # print(f"{d}: new={len(app_d)}, N={len(map_by_dep[d])}")


n = int(input())
apps = load_data()
sort_gpa()
map_by_dep = {d: [] for d in departments}
dep_to_do = copy(departments)
rank = 0
while apps and dep_to_do and rank < 3:
    rank += 1
    dep = copy(dep_to_do)
    for d in dep:
        choise_by_rank(d, rank)

for d in sorted(map_by_dep):
    print(f"\n{d}")
    map_by_dep[d].sort(key=lambda x: (-float(x[2]), x[0], x[1]))
    for a in map_by_dep[d]:
        print(*a[:3])
