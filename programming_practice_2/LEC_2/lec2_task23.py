import csv
with open('txt/average-latitude-longitude-countries.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    country_list = []
    location_list = []
    for row in reader:
        country_code, country_name, latitude, longitude = row
        country_list.append((country_code, country_name))
        location_list.append((country_code, (float(latitude), float(longitude))))
    print(country_list)
    print(location_list)

    print([c[1] for c, l in zip(country_list, location_list) if l[1][0] < 0])
    input_code = input("Enter the code of the country: ")
    for code, name in country_list:
        if code == input_code:
            print(f"Country: {name}")

print("================================================")

with open("txt/class_enrollment.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    from collections import defaultdict
    enrollment_dict = defaultdict(set)
    for row in reader:
        course, student = row
        enrollment_dict[course].add(student)

    def math_addicts():
        math_courses = ["MAS101", "MAS201", "MAS212"]
        math_students = set.intersection(*[enrollment_dict[course] for course in math_courses])
        return math_students

    def only_cc511():
        return enrollment_dict["CC511"] - set.union(*[enrollment_dict[course] for course in enrollment_dict if course != "CC511"])

    print("Students enrolled in all math courses:", math_addicts())
    print("Students enrolled only in CC511:", only_cc511())
