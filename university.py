from copy import copy

departments = {'Biotech': [0, 1], 'Chemistry': [1], 'Engineering': [2, 3], 'Mathematics': [2], 'Physics': [0, 2]}
exams = {'physics', 'chemistry', 'math', 'computer science'}

def load_data():
    list = []
    with open('applicants.txt') as file:
        for ln in file:
            list.append(ln.split())
    return list

# k in [0..3] - exams list
def sort_exam(list, ex):
    list.sort(key=lambda x: (-mean_score(x, ex), x[0], x[1]))

# a - student info, ex - exams list
def mean_score(a, ex):
    sum = 0
    for x in ex:
        sum += float(a[x + 2])
    return max(sum / len(ex), float(a[6]))

# d - department, 1..3 - rank
def choise_by_rank(d, rank):
    ex = departments[d]
    n1 = n - len(map_by_dep[d])
    sort_exam(apps, ex)
    app_d = [a for m, a in enumerate(filter(lambda x: x[rank + 6] == d, apps)) if m < n1]
    map_by_dep[d] += app_d
    for a in app_d:
        apps.remove(a)
    if len(map_by_dep[d]) == n:
        dep_to_do.remove(d)

def save_data():
    for d in sorted(map_by_dep):
        ex = departments[d]
        sort_exam(map_by_dep[d], ex)
        fn = d.lower() + ".txt"
        print(f"\n{d}")
        with open(fn, "w") as file:
            for a in map_by_dep[d]:
                file.write(f"{a[0]} {a[1]} {mean_score(a, ex)}\n")
                print(f"{a[0]} {a[1]} {mean_score(a, ex)}")


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
save_data()
