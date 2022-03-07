def load_data(m):
    list = []
    for _ in range(m):
        list.append(input().split(' '))
    return list

def sort_gpa():
    apps.sort(key=lambda x: (-float(x[2]), x[0], x[1]))


n = int(input())
m = int(input())
apps = load_data(n)
sort_gpa()
print('Successful applicants:')
for a in apps[:m]:
    print(*a[:2])
