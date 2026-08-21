# Week 3 - Activity 3: ER Description

## Description
This ER diagram models the daily operations of a university/college course management. At the core of the system are the scheduled **Lectures**, which act as the hub connecting students and teaching staff. When a **Student** decides to take a class, an **Enrollment** record is given or generated. This allows the school to track which students are registered for which specific lecture sessions, along with the date they enrolled. 

The system organizes the academic staff. It tracks each **Lecturer** and the overarching **Subjects** they are qualified to teach. These teaching assignments became active when a Lecturer is scheduled to deliver a specific Subject during a specific **Lecture** time and date. The top half of the diagram manages "who is learning," while the other bottom half manages "who is teaching."

---

## Additional Attributes
Adding the following attributes would enhance the system's ability to communicate with the students:

* **Entity:** `Student`
    * **New Attribute 1:** `Email_address` (To allow the university to contact the student by email).
    * **New Attribute 2:** `Phone_number` (For emergency contacts or urgent updates for their classes).

---

## Relationship Types and Descriptions
The diagram uses a combination of diamonds and "crow's feet" notation. Both central diamonds connect three distinct entities, making them structurally **Ternary Relationships**. Logically, they function to resolve **Many-to-Many** scenarios.

* **The "Enrolls" Relationship:**
    * **Type:** Ternary Relationship (Many-to-Many).
    * **Description:** This relationship connects a `Student`, a `Lecture`, and an `Enrollment` record. The "crow's feet" symbols indicate the "many" cardinality. It acts as a many-to-many connection because a student can enroll in multiple lectures, and a single lecture session can have multiple students. The `Enrollment` acts as a bridge to store the specific details (like the date) of that connection.

* **The "Lectures" Relationship:** 
    * **Type:** Ternary Relationship (Many-to-Many).
    * **Description:** This connects a `Lecturer`, `Subjects`, and a `Lecture`. It dictates that a lecturer can teach multiple subjects and deliver multiple lectures, while a subject can be taught by multiple lecturers. The relationship links the specific teacher, the general subject material, and the actual scheduled lecture event together.