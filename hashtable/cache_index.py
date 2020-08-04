employees = [
    ('Jill', 'Sales'),
    ('Betty', 'Manager'),
    ('Kristin', 'Sales'),
    ('Mia', 'Manager')
]

index = {}

def build_index():
    for e in employees:
        dept = e[1]

        if dept not in index:
            index[dept]= []
            
        index[dept].append(e)
build_index()
print(employees, index)

while True:
    dept = input('Enter department:')
    print(index[dept])
    

