from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from addiction_logic import detect_addiction

app = Flask(__name__)

def get_db():
    db_path = os.path.join("/tmp", "database.db")
    return sqlite3.connect(db_path)


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usage_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            screen_time REAL,
            social_time REAL,
            app_opens INTEGER,
            night_usage TEXT,
            risk_level TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    screen_time = float(request.form["screen_time"])
    social_time = float(request.form["social_time"])
    app_opens = int(request.form["app_opens"])
    night_usage = request.form["night_usage"]

    risk = detect_addiction(screen_time, social_time, app_opens, night_usage)

    conn = get_db()
    conn.execute("""
        INSERT INTO usage_data 
        (screen_time, social_time, app_opens, night_usage, risk_level)
        VALUES (?, ?, ?, ?, ?)
    """, (screen_time, social_time, app_opens, night_usage, risk))
    conn.commit()
    conn.close()

    return render_template("result.html", risk=risk)

@app.route("/history")
def history():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM usage_data ORDER BY id DESC")
    logs = cursor.fetchall()
    conn.close()
    return render_template("history.html", logs=logs)

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.json
    risk = detect_addiction(
        data["screen_time"],
        data["social_time"],
        data["app_opens"],
        data["night_usage"]
    )
    return jsonify({"risk_level": risk})

