from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        conn = pg8000.connect(user="shaxzodbek", password="shox777", host="localhost", port=5432, database="miniproj")
        cur = conn.cursor()
        query = "SELECT course_name, day, time, room FROM timetable;"
        cur.execute(query)
        courses = cur.fetchall()
    except Exception as e:
        courses = []
        print(f"Error fetching courses: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

    return render_template("index.html", courses=courses)



if __name__ == "__main__":
    app.run(debug=True)
