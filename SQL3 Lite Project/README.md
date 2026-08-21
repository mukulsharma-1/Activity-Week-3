# Week 3 - Database Design and Implementation

## Activity 3: ER Diagram Analysis
This ER diagram models a university course management. The top half manages "who is learning" by tracking Students and their class registrations, while the bottom half manages "who is teaching" by tracking Lecturers and the Subjects they deliver.

**Additional Attributes: Proposed**
* **Entity:** `Student` -> **Attributes:** `Email_address` and `Phone_number` (to enable direct communication with enrolled students).

**Relationship Types:**
Both relationships are structurally **Ternary**, operating with **Many-to-Many** to form complete records.
* **The "Enrolls" Relationship:** Connects `Student`, `Lecture`, and `Enrollment`. A student takes multiple lectures, and a lecture has multiple students. `Enrollment` bridges them to store the registration date.
* **The "Lectures" Relationship:** Connects `Lecturer`, `Subjects`, and `Lecture`. A lecturer teaches multiple subjects, and subjects are taught by multiple lecturers. 

---

## Activity 4: SQLite3 Database Implementation
To transition the conceptual ER diagram into a functional SQLite3 relational database, Primary Keys (PK) and Foreign Keys (FK) were used. 

**ER to Relational Schema:**
* **Resolving "Enrolls":** Implemented physically as the `Enrollments` table. It bridges the gap by linking `Student_code` (FK) to the specific lecture `CC_number` (FK).
* **Resolving "Lectures":** The `Lectures` entity uses `CC_number` as its PK and acts as a bridge by pulling in `Subject_code` (FK) and `Lecturer_id` (FK).

---

## Project Structure & Setup
The Python implementation is divided into three files for clean execution and logic separation:
* **`database_setup.py`**: Defines table schemas and handles hard-coded data insertion.
* **`queries.py`**: Houses the SQL `SELECT` statements required by the assignment.
* **`main.py`**: The main orchestrator that connects to the database and runs the setup and query modules.

### Fulfillment of Assignment Criteria
The database is hard-coded to automatically populate with the exact data quantities:

* **5 Students:** 
  1. Alice Smith (S001)
  2. Bob Jones (S002)
  3. Charlie Brown (S003)
  4. Diana Prince (S004)
  5. Evan Wright (S005)
* **2 Lecturers:** 
  1. Alan Turing (L01)
  2. Ada Lovelace (L02)
* **3 Courses (Subjects):** 
  1. Intro to Programming (CS101)
  2. Database Systems (DB201)
  3. Web Development (WD301)
* **Appropriate Additional Records:** 
  * 3 specific **Lecture** records were created to link the Lecturers to the Courses.
  * 8 specific **Enrollment** records were created to link the Students to the Lectures (ensuring some students take multiple courses).

### Generated Database File
This project utilizes **SQLite3**, executing the code will automatically generate a single, serverless file named `university.db` in the root directory containing all the schema and data listed above.

### How to Run & Expected Output
Execute `python main.py` in your terminal. The output generated will prove that the data was inserted:

```text
Starting University Database Program...

Tables created successfully.
Sample data inserted successfully.

--- Students Registered per Course ---
Course: Intro to Programming | Registered Students: 3
Course: Database Systems | Registered Students: 3
Course: Web Development | Registered Students: 2

--- Students Enrolled in > 1 Course ---
ID: S001 | Name: Alice Smith | Courses Enrolled: 2
ID: S002 | Name: Bob Jones | Courses Enrolled: 2
ID: S004 | Name: Diana Prince | Courses Enrolled: 2

Database connection closed. Program complete.