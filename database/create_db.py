import sqlite3

# ==================== DATABASE INITIALIZATION SCRIPT ====================
# The function below creates all the required tables for the app.
# It is safe to run multiple times and won't overwrite existing tables.
def create_db():
    con = sqlite3.connect(database="rms.db")  # create connection
    cur = con.cursor()  # create cursor from connection
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")
    con.commit()   #commit on the connection

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS studentresult(sid INTEGER PRIMARY KEY AUTOINCREMENT,first_name text, last_name text, contact text, email text, security_question text, security_answer text, password text)")
    con.commit()

    
    con.close()   #Good practice to close the connection





if __name__ == "__main__":
    # Run script in standalone mode to initialize database.
    create_db()
