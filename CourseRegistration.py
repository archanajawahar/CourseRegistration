class CourseRegistration:

    def __init__(self):
        # Course details
        self.courses = {
            "DBMS": {
                "credits": 4,
                "prerequisite": "Programming",
                "capacity": 2,
                "semester": 3,
                "time": "09:00-10:00"
            },

            "AI": {
                "credits": 4,
                "prerequisite": "Data Structures",
                "capacity": 2,
                "semester": 3,
                "time": "10:00-11:00"
            },

            "ML": {
                "credits": 3,
                "prerequisite": "Statistics",
                "capacity": 2,
                "semester": 3,
                "time": "09:00-10:00"
            },

            "Cloud": {
                "credits": 3,
                "prerequisite": "Networking",
                "capacity": 2,
                "semester": 4,
                "time": "11:00-12:00"
            }
        }

        self.max_credits = 8

        # Stores registered students
        self.registrations = {}

    def register_student(self, student_id, program, semester,
                          courses_selected, completed_courses):

        # Create student record
        if student_id not in self.registrations:
            self.registrations[student_id] = []

        registered_courses = self.registrations[student_id]

        total_credits = 0
        selected_times = []

        # Check each selected course
        for course in courses_selected:

            # Invalid course
            if course not in self.courses:
                return "Invalid course: " + course

            details = self.courses[course]

            # Semester restriction
            if semester != details["semester"]:
                return "Semester restriction for " + course

            # Duplicate registration
            if course in registered_courses:
                return "Duplicate registration: " + course

            # Prerequisite check
            prerequisite = details["prerequisite"]

            if prerequisite not in completed_courses:
                return "Missing prerequisite for " + course

            # Course capacity
            if len(registered_courses) >= details["capacity"]:
                return "Course is full: " + course

            # Timetable clash
            if details["time"] in selected_times:
                return "Timetable conflict: " + course

            selected_times.append(details["time"])

            total_credits += details["credits"]

        # Credit limit
        if total_credits > self.max_credits:
            return "Credit limit exceeded"

        # Register courses
        for course in courses_selected:
            registered_courses.append(course)

        return "Registration successful"

    def total_registered_credits(self, student_id):

        if student_id not in self.registrations:
            return 0

        total = 0

        for course in self.registrations[student_id]:
            total += self.courses[course]["credits"]

        return total

    def display_registration(self, student_id):

        if student_id not in self.registrations:
            return "No registration found"

        return self.registrations[student_id]


# ---------------- MAIN PROGRAM ----------------

system = CourseRegistration()

result = system.register_student(
    student_id="S101",
    program="CSE",
    semester=3,
    courses_selected=["DBMS"],
    completed_courses=["Programming"]
)

print(result)

print("Registered Courses:",
      system.display_registration("S101"))

print("Total Credits:",
      system.total_registered_credits("S101"))
