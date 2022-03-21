from flask import Flask, render_template, request, redirect
from database import Database
from datetime import datetime, timedelta

app = Flask(__name__)


def days(day):
    day_list = [datetime.fromisoformat(day) + timedelta(days=i) for i in range(-2, 3)]
    return day_list


@app.route("/")
def index():
    selected_day = request.args.get("day") if request.args.get("day") else datetime.now().isoformat()
    selected_day_short = int(datetime.fromisoformat(selected_day).strftime("%Y%m%d"))
    _days = days(selected_day)
    habits = Database.find_from_db("habits", {})
    habits = [
        habit for habit in habits
        if habit["date"] <= selected_day_short
    ]
    completed_habits = Database.find_from_db("completion", {"date": selected_day_short})
    if completed_habits:
        for habit in habits:
            if habit["content"] in completed_habits[0]["completed"]:
                habit.update({"status": "completed"})
            else:
                habit.update({"status": "uncompleted"})
    print("habits:", habits)
    print("completed_habits:", completed_habits)
    return render_template("index.html", habits=habits, days=_days, selected_day=selected_day_short)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = {
            "content": request.form["content"],
            "date": int(datetime.now().strftime("%Y%m%d"))
        }
        Database.insert_to_db("habits", data) if data["content"] else None
        return redirect("/")
    return render_template("add_habit.html")


@app.route("/complete", methods=["POST"])
def complete():
    habit = request.form.get("habit")
    date = int(request.form.get("date"))
    completed_habits = Database.find_from_db("completion", {"date": date})
    if not completed_habits:
        Database.insert_to_db("completion", {"date": date, "completed": [habit]})
    elif habit not in completed_habits[0]["completed"]:
        completed = completed_habits[0]["completed"]
        completed.append(habit)
        Database.update_record(
            "completion",
            completed_habits[0]["_id"],
            {"completed": completed}
        )
    return redirect(f"/?day={datetime.strptime(str(date), '%Y%m%d')}")


if __name__ == "__main__":
    app.run()
