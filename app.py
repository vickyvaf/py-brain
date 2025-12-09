from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection
import sqlite3

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    user = None
    if "user_id" in session:
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (session["user_id"],)).fetchone()
        conn.close()
    
    return render_template("index.html", user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("home"))
        
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password")
            
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("home"))
        
    username = request.form["username"]
    password = request.form["password"]
    
    if not username or not password:
        flash("Username and password are required")
        return redirect(url_for("login"))
        
    hashed_password = generate_password_hash(password)
    
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        flash("Registration successful! Please login.")
    except sqlite3.IntegrityError:
        flash("Username already exists")
    finally:
        conn.close()
        
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

import random
from questions import questions_data, get_question

@app.route("/quiz")
def quiz():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    question = random.choice(questions_data)
    return render_template("quiz.html", username=session.get("username"), question=question)

@app.route("/quiz/check", methods=["POST"])
def check_answer():
    if "user_id" not in session:
        return redirect(url_for("login"))
        
    question_id = int(request.form["question_id"])
    selected_option = request.form["option"]
    
    question = get_question(question_id)
    
    if not question:
        flash("Error: Question not found.")
        return redirect(url_for("quiz"))
        
    is_correct = (selected_option == question["answer"])
    
    if is_correct:
        flash("Correct! +10 Brain Points")
        conn = get_db_connection()
        conn.execute('INSERT INTO scores (user_id, score) VALUES (?, ?)', (session["user_id"], 10))
        conn.commit()
        conn.close()
    else:
        flash(f"Wrong! The correct answer was {question['answer']}.")
        
    return redirect(url_for("quiz"))

@app.route("/leaderboard")
def leaderboard():
    conn = get_db_connection()
    leaders = conn.execute('''
        SELECT u.username, SUM(s.score) as total_score 
        FROM scores s 
        JOIN users u ON s.user_id = u.id 
        GROUP BY u.id 
        ORDER BY total_score DESC 
        LIMIT 10
    ''').fetchall()
    conn.close()
    return render_template("leaderboard.html", leaders=leaders)

if __name__ == "__main__":
    app.run(debug=True)
