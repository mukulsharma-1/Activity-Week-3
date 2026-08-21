import sqlite3

def create_tables(conn):
    """Creates the necessary database tables based on the ER diagram."""
    cursor = conn.cursor()
    
    # Using executescript to run multiple SQL commands at once
    # Hardcoded data
    cursor.executescript('''
        -- 1. Students Table
        CREATE TABLE IF NOT EXISTS Students (
            Student_code TEXT PRIMARY KEY,
            F_name TEXT,
            L_name TEXT,
            NID TEXT,
            B_date TEXT
        );

        -- 2. Lecturers Table
        CREATE TABLE IF NOT EXISTS Lecturers (
            Lecturer_id TEXT PRIMARY KEY,
            L_firstname TEXT,
            L_lastname TEXT,
            L_email TEXT,
            L_address TEXT
        );

        -- 3. Subjects Table
        CREATE TABLE IF NOT EXISTS Subjects (
            Subject_code TEXT PRIMARY KEY,
            Subject_name TEXT,
            Subject_unit INTEGER
        );

        -- 4. Lectures Table (The central hub connecting Subject and Lecturer)
        CREATE TABLE IF NOT EXISTS Lectures (
            CC_number TEXT PRIMARY KEY,
            Subject_code TEXT,
            Lecturer_id TEXT,
            Lecture_name TEXT,
            Date TEXT,
            Time TEXT,
            FOREIGN KEY(Subject_code) REFERENCES Subjects(Subject_code),
            FOREIGN KEY(Lecturer_id) REFERENCES Lecturers(Lecturer_id)
        );

        -- 5. Enrollments Table (The bridge connecting Student and Lecture)
        CREATE TABLE IF NOT EXISTS Enrollments (
            Enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_code TEXT,
            CC_number TEXT,
            Date_of_enrolment TEXT,
            FOREIGN KEY(Student_code) REFERENCES Students(Student_code),
            FOREIGN KEY(CC_number) REFERENCES Lectures(CC_number)
        );
    ''')
    print("Tables created successfully.")

def insert_sample_data(conn):
    """Populates the database tables with required sample data."""
    cursor = conn.cursor()
    
    # Data for 5 Students
    students = [
        ('S001', 'Alice', 'Smith', 'NID111', '2000-01-15'),
        ('S002', 'Bob', 'Jones', 'NID222', '1999-11-20'),
        ('S003', 'Charlie', 'Brown', 'NID333', '2001-03-10'),
        ('S004', 'Diana', 'Prince', 'NID444', '2000-07-25'),
        ('S005', 'Evan', 'Wright', 'NID555', '1998-12-05')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Students VALUES (?,?,?,?,?)', students)

    # Data for 2 Lecturers
    lecturers = [
        ('L01', 'Alan', 'Turing', 'alan@uni.edu', '123 Tech St'),
        ('L02', 'Ada', 'Lovelace', 'ada@uni.edu', '456 Logic Ave')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Lecturers VALUES (?,?,?,?,?)', lecturers)

    # Data for 3 Subjects (Courses)
    subjects = [
        ('CS101', 'Intro to Programming', 3),
        ('DB201', 'Database Systems', 4),
        ('WD301', 'Web Development', 3)
    ]
    cursor.executemany('INSERT OR IGNORE INTO Subjects VALUES (?,?,?)', subjects)

    # Data for Lecture Sessions
    lectures = [
        ('CC001', 'CS101', 'L01', 'Programming Mon/Wed', 'Mon-Wed', '10:00 AM'),
        ('CC002', 'DB201', 'L02', 'Databases Tue/Thu', 'Tue-Thu', '01:00 PM'),
        ('CC003', 'WD301', 'L01', 'Web Dev Friday', 'Friday', '09:00 AM')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Lectures VALUES (?,?,?,?,?,?)', lectures)

    # Data for Enrollments 
    # Ensuring some students have >1 course for our queries later
    enrollments = [
        ('S001', 'CC001', '2023-09-01'), # Alice in CS101
        ('S001', 'CC002', '2023-09-01'), # Alice in DB201
        ('S002', 'CC002', '2023-09-02'), # Bob in DB201
        ('S002', 'CC003', '2023-09-02'), # Bob in WD301
        ('S003', 'CC001', '2023-09-03'), # Charlie in CS101
        ('S004', 'CC001', '2023-09-04'), # Diana in CS101
        ('S004', 'CC003', '2023-09-04'), # Diana in WD301
        ('S005', 'CC002', '2023-09-05')  # Evan in DB201
    ]
    cursor.executemany('INSERT OR IGNORE INTO Enrollments (Student_code, CC_number, Date_of_enrolment) VALUES (?,?,?)', enrollments)

    # Save (commit) the changes to the database
    conn.commit()
    print("Sample data inserted successfully.")