import os
from flask import Flask

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anurag12345#'
app.config['MYSQL_DB'] = 'Resumes'

mysql = MySQL(app)


@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        if request.method == 'POST':
            # Get the form data
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            resume_file = request.files['resume']

            # Save the file to the server
            #filename = secure_filename(resume.filename)
            #resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # Insert the user data into the database
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        
            Upload_folder = os.path.join(os.getcwd(), "uploads", "resumes")
            if not os.path.exists(Upload_folder):
                os.makedirs(Upload_folder)
            file_path = os.path.join(Upload_folder, resume_file.filename)
            resume_file.save(file_path)

            # Insert the resume data into the database
            cur.execute("INSERT INTO resumes (filename) VALUES (%s)", (file_path,))

            mysql.connection.commit()
            cur.close()
            
            # Return a success message
            return render_template('successful.html')
    except:
        return render_template('failed.html')
    
    # Render the signup form
    return render_template('signup.html')

#@app.route('/upload_resume', methods=['GET', 'POST'])
# def upload_resume():
#     if request.method == 'POST':
#         # Get the uploaded file
#         resume = request.files['resume']
        
#         # Save the file to the server
#         filename = secure_filename(resume.filename)
#         resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         # Insert the resume data into the database
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO resumes (filename) VALUES (%s)", (filename,))
#         mysql.connection.commit()
#         cur.close()
        
#         # Return a success message
#         return 'Resume uploaded successfully!'
    
#     # Render the resume upload form
#     return render_template('signup.html')



if __name__ == '__main__':
   app.run()