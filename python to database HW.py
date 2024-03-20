#!/usr/bin/env python
# coding: utf-8

# In[93]:


import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="komali",
    database="student_demo"
)
print(db_connection)


# In[59]:


# db_connection.close()


# In[85]:


def menu_display():
    print("\nMenu:")
    print("1)Add a new student record")
    print("2)Update an existing student record")
    print("3)Delete a student record")
    print("4)View all student records")
    print("5)Exit the program")


# In[86]:


def add_student_record(cursor):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, age, grade))
    print("student record added successfully")


# In[87]:


cursor = db_connection.cursor()
add_student_record(cursor)


# In[88]:


cursor.close()
db_connection.commit()


# In[70]:


def update_student_record(cursor):
    student_id = int(input("Enter student ID to update: "))
    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    new_grade = input("Enter new grade: ")
    sql = "UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s"
    cursor.execute(sql, (new_name, new_age, new_grade, student_id))
    print("Student record updated successfully")


# In[71]:


cursor = db_connection.cursor()
update_student_record(cursor)


# In[72]:


cursor.close()
db_connection.commit()


# In[76]:


def delete_student_record(cursor):
    student_id = int(input("Enter student ID to delete: "))
    sql = "DELETE FROM students WHERE id=%s"
    cursor.execute(sql, (student_id,))
    print("Student record deleted successfully")


# In[77]:


cursor = db_connection.cursor()
delete_student_record(cursor)


# In[78]:


cursor.close()
db_connection.commit()


# In[89]:


def view_all_student_records(cursor):
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if not records:
        print("No student records found.")
    else:
        print("\nAll Student Records:")
        for record in records:
            print(record)


# In[90]:


cursor = db_connection.cursor()
view_all_student_records(cursor)


# In[91]:


cursor.close()
db_connection.commit()


# In[97]:


while True:
            menu_display()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                add_student_record(cursor)
            elif choice == "2":
                update_student_record(cursor)
            elif choice == "3":
                delete_student_record(cursor)
            elif choice == "4":
                view_all_student_records(cursor)
            elif choice == "5":
                print("Exiting the program")
                break
            else:
                print("Invalid choice! Please enter a number from 1 to 5")


# In[96]:


cursor = db_connection.cursor()
db_connection.commit()


# In[98]:


cursor.close()
db_connection.close()


# In[ ]:





# In[ ]:




