from CourseRegistration import CourseRegistration


print("===== COURSE REGISTRATION QA =====")


# 1. Valid registration
print("\n1. Valid Registration")

system = CourseRegistration()

print(system.register_student(
    "S101",
    "CSE",
    3,
    ["DBMS"],
    ["Programming"]
))

print("Credits:",
      system.total_registered_credits("S101"))


# 2. Missing prerequisite
print("\n2. Missing Prerequisite")

system = CourseRegistration()

print(system.register_student(
    "S102",
    "CSE",
    3,
    ["DBMS"],
    []
))


# 3. Credit-limit violation
print("\n3. Credit-Limit Violation")

system = CourseRegistration()

print(system.register_student(
    "S103",
    "CSE",
    3,
    ["DBMS", "AI"],
    ["Programming", "Data Structures"]
))


# 4. Timetable conflict
print("\n4. Timetable Conflict")

system = CourseRegistration()

print(system.register_student(
    "S104",
    "CSE",
    3,
    ["DBMS", "ML"],
    ["Programming", "Statistics"]
))


# 5. Full course
print("\n5. Full Course")

system = CourseRegistration()

print(system.register_student(
    "S105",
    "CSE",
    3,
    ["DBMS"],
    ["Programming"]
))

print(system.register_student(
    "S106",
    "CSE",
    3,
    ["DBMS"],
    ["Programming"]
))

print(system.register_student(
    "S107",
    "CSE",
    3,
    ["DBMS"],
    ["Programming"]
))


# 6. Duplicate registration
print("\n6. Duplicate Registration")

system = CourseRegistration()

print(system.register_student(
    "S108",
    "CSE",
    3,
    ["DBMS"],
    ["Programming"]
))

print(system.register_student(
    "S108",
    "CSE",
    3,
    ["DBMS"],
    ["Programming"]
))


# 7. Invalid course
print("\n7. Invalid Course")

system = CourseRegistration()

print(system.register_student(
    "S109",
    "CSE",
    3,
    ["CyberSecurity"],
    []
))


# 8. Semester restriction
print("\n8. Semester Restriction")

system = CourseRegistration()

print(system.register_student(
    "S110",
    "CSE",
    4,
    ["DBMS"],
    ["Programming"]
))


# 9. Boundary credit values
print("\n9. Boundary Credit Values")

system = CourseRegistration()

print(system.register_student(
    "S111",
    "CSE",
    3,
    ["DBMS", "AI"],
    ["Programming", "Data Structures"]
))

print("Total Credits:",
      system.total_registered_credits("S111"))


print("\n===== QA COMPLETED =====")
