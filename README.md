# Student Result Management System (SRMS)

A comprehensive desktop application built with Python and Tkinter for managing student results, courses, and user authentication. This system allows administrators to add/manage courses, students, and their results, while providing a secure login system with password recovery.

## 📋 Features

### 🔐 Authentication System
- User registration with security questions
- Secure login with email/password
- Password recovery via security questions
- Session management with logout functionality

### 📚 Course Management
- Add, update, delete courses
- Search courses by name
- View all courses in a table format
- Course details: name, duration, charges, description

### 👨‍🎓 Student Management
- Add, update, delete student records
- Search students by roll number
- Comprehensive student information:
  - Personal details (name, email, gender, DOB, contact)
  - Address information (state, city, PIN)
  - Course enrollment
- View all students in a table format

### 📊 Result Management
- Add student results with marks and full marks
- Automatic percentage calculation
- Prevent duplicate results for same student-course combination
- Search students by roll number to add results

### 📈 Report Viewing
- View individual student results
- Search results by roll number
- Delete result records
- Display: roll, name, course, marks obtained, total marks, percentage

### 🎯 Dashboard
- Real-time counters for total courses, students, and results
- Quick navigation buttons to all modules
- Professional UI with background images and icons

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework
- **SQLite3** - Local database for data storage
- **Pillow (PIL)** - Image processing for UI elements
- **Subprocess** - For launching different application windows

## 📁 Project Structure

```
RMS/
├── login.py              # Login and authentication window
├── register.py           # User registration window
├── dashboard.py          # Main application dashboard
├── course.py             # Course management module
├── student.py            # Student management module
├── result.py             # Result entry module
├── report.py             # Result viewing and deletion module
│
├── database/             # Database initialization script 
│   └── create_db.py 
│      
├── assets/               # UI images and icons
│   ├── bgimg.png
│   ├── side.png
│   ├── logo_p.png
│   ├── student.png
│   ├── result2.png
│   ├── course-page.png        # Screenshot course page
│   ├── home-page.png          # Screenshot home page
│   ├── login-page.png         # Screenshot login page
│   ├── logout-page.png        # Screenshot logout page
│   ├── register-page.png      # Screenshot register page
│   ├── result-page.png        # Screenshot result page
│   ├── student-page.png       # Screenshot student page
│   └── view-student-page.png      # Screenshot view student result page
│
└── rms.db               # SQLite database (created automatically)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Step 1: Clone or Download
```bash
# If uploading to GitHub, clone your repository
git clone https://github.com/ranjeetkannaujiya/student-result-management-system.git
cd student-result-management-system
```

### Step 2: Install Dependencies
```bash
pip install pillow
```

### Step 3: Initialize Database
Run the database creation script first:
```bash
python create_db.py
```
This will create `rms.db` with all required tables.

### Step 4: Run the Application
Start the application by running the login window:
```bash
python login.py
```

## 📖 Usage Guide

### First Time Setup
1. Run `create_db.py` to set up the database
2. Run `login.py` to start the application
3. Click "Register new Account?" to create your first admin account
4. Fill in all registration details and agree to terms
5. Login with your new credentials

### Daily Operations

#### Adding Courses
1. From dashboard, click "Course" button
2. Fill course details (name, duration, charges, description)
3. Click "Save" to add the course

#### Managing Students
1. Click "Student" from dashboard
2. Fill student information (personal details, address, course)
3. Select course from dropdown (courses must be added first)
4. Click "Save" to add student

#### Entering Results
1. Click "Result" from dashboard
2. Select student roll number from dropdown
3. Click "Search" to populate student details
4. Enter marks obtained and full marks
5. Click "Submit" to save result

#### Viewing Results
1. Click "View Student Result" from dashboard
2. Enter roll number and click "Search"
3. View result details or click "Delete" to remove

## 🗄️ Database Schema

### Tables Created:
- **course**: Course information (cid, name, duration, charges, description)
- **student**: Student details (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address)
- **result**: Student results (rid, roll, name, course, marks_ob, full_marks, per)
- **studentresult**: User accounts (sid, first_name, last_name, contact, email, security_question, security_answer, password)

## 🔧 Troubleshooting

### Common Issues:
1. **"python command not found"**: Ensure Python is installed and in PATH
2. **"Module not found"**: Install required packages with `pip install pillow`
3. **"Database error"**: Run `create_db.py` first to initialize database
4. **"Image not found"**: Ensure Images folder is in the same directory as scripts

### Database Reset:
If you need to reset the database:
```bash
# Delete rms.db file and run create_db.py again
rm rms.db
python create_db.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ranjeet** - *Initial work* - [Your GitHub Profile](https://github.com/ranjeetkannaujiya)

## 🙏 Acknowledgments

- Tkinter documentation
- SQLite3 tutorials
- Pillow library documentation
- Open source community

---

**Note**: This desktop application is developed for educational institutions to efficiently manage and maintain student result records. It stores important student data, so regular database backup is recommended to prevent data loss.
