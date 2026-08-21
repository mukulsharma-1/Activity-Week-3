import sqlite3

def students_per_course(conn):
    """Answers: How many students are registered in each course?"""
    cursor = conn.cursor()
    
    # Join Subjects -> Lectures -> Enrollments to count students
    query = '''
        SELECT s.Subject_name, COUNT(e.Student_code) AS Student_Count
        FROM Subjects s
        JOIN Lectures l ON s.Subject_code = l.Subject_code
        JOIN Enrollments e ON l.CC_number = e.CC_number
        GROUP BY s.Subject_name;
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("\n--- Students Registered per Course ---")
    for row in results:
        print(f"Course: {row[0]} | Registered Students: {row[1]}")


def students_multiple_courses(conn):
    """Answers: List the names and student IDs of students enrolled in more than one course."""
    cursor = conn.cursor()
    
    # Join Students -> Enrollments and use HAVING to filter > 1
    query = '''
        SELECT st.Student_code, st.F_name, st.L_name, COUNT(e.CC_number) AS Course_Count
        FROM Students st
        JOIN Enrollments e ON st.Student_code = e.Student_code
        GROUP BY st.Student_code
        HAVING COUNT(e.CC_number) > 1;
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("\n--- Students Enrolled in > 1 Course ---")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Courses Enrolled: {row[3]}")