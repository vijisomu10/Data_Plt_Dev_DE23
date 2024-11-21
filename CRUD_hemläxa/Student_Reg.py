import sqlite3

conn = sqlite3.connect(
    "C:\\Users\\vijis\\Data_platform_development\\SQL Lite\\student_details.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS student_reg(
                student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT UNIQUE,
                last_name TEXT UNIQUE,
                email TEXT,
                addres TEXT,
                mobile_number INTEGER)''')

def create_student():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    mobile_number = input("Enter your mobile number: ")
    
    cur.execute('''
                SELECT * FROM student_reg 
                WHERE 
                first_name = ? AND last_name = ?''', 
                (first_name, last_name))
    existing_student = cur.fetchone()
    
    if existing_student:
        print('student already exists')
    else:        
        cur.execute('''
                    INSERT OR IGNORE INTO student_reg
                    (first_name, last_name, email, addres, mobile_number)
                    VALUES(?,?,?,?,?)''', 
                    (first_name, last_name, email, address, mobile_number)
                    )
        
        print(first_name, last_name, email, address, mobile_number)

def view_students():
    stu_list = cur.execute('''SELECT * FROM student_reg''')
    for list in stu_list:
        print(list)

while True:
    print('Welcome to Student Registration!')
    print('1. Register/Create student details')
    print("2. View Student's details")
    print('3. Update student details')
    print('4. Delete student details')
    print('5. View deleted student details')
    print('6. Exit the registration')
    choose_menu = input('Choose from the above menu: ')
    
    if choose_menu == '1':
        create_student()
        conn.commit()
        print("Student registered successfully")
    
    elif choose_menu == '2':
        view_students()
        
    elif choose_menu == '3':        
        user_id = input('Enter your student id: ')
        column_to_update = input(
            'Enter the column to update(first_name, last_name, email, addres, mobile_number):'
            )
        new_input = input('Enter the new value:')
        up_date = cur.execute(f'''
                                UPDATE student_reg SET {column_to_update} = ?
                                WHERE student_id = ?
                                ''', 
                                (new_input, user_id))
        conn.commit()

    elif choose_menu == '4':
        del_student = input('Enter student id to delete the information:')
        cur.execute(f'''DELETE FROM student_reg WHERE student_id = {del_student} ''')
        conn.commit()
    
    elif choose_menu == '5':
        pass
    
    elif choose_menu == '6':
        exit()
            
    else:
        print('Please choose from the valid one!')

conn.commit()
conn.close()
    