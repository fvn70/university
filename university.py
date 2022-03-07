from copy import copy

departments = {'Biotech': 1, 'Chemistry': 1, 'Engineering': 3, 'Mathematics': 2, 'Physics': 0}
exams = {'physics', 'chemistry', 'math', 'computer science'}

def load_data():
    list = []
    with open('applicans.txt') as file:
        for ln in file:
            list.append(ln.split())
    return list


# k in [0..3] - exams list
def sort_exam(list, k):
    list.sort(key=lambda x: (-float(x[k + 2]), x[0], x[1]))


# d - department, k = 1..3 - rank
def choise_by_rank(d, rank):
    ex = departments[d]
    n1 = n - len(map_by_dep[d])
    sort_exam(apps, ex)
    app_d = [a for m, a in enumerate(filter(lambda x: x[rank + 5] == d, apps)) if m < n1]
    map_by_dep[d] += app_d
    for a in app_d:
        apps.remove(a)
    if len(map_by_dep[d]) == n:
        dep_to_do.remove(d)


n = int(input())
apps = load_data()
map_by_dep = {d: [] for d in departments}
dep_to_do = list(departments.keys())
rank = 0

while apps and dep_to_do and rank < 3:
    rank += 1
    dep = copy(dep_to_do)
    for d in dep:
        choise_by_rank(d, rank)

for d in sorted(map_by_dep):
    print(f"\n{d}")
    exam = departments[d]
    sort_exam(map_by_dep[d], exam)
    for a in map_by_dep[d]:
        print(f"{a[0]} {a[1]} {a[exam + 2]}")
