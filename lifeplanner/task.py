from flask import Flask, render_template, Blueprint, request, flash
from flask_session import Session



task = Blueprint('task', __name__)

tasks = []
max_tasks=6
@task.route("/todo", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        new_task = request.form.get("input_bar")
        print(new_task)
        if new_task!='' and len(tasks)<max_tasks:
            tasks.append(new_task)
        elif len(tasks)==max_tasks:
             flash("You Have Riched The Limit" , category='error')
        else:
            flash("Add Task First" , category='error')


    return render_template('todo.html', tasks=tasks)
def delete():
    pass
def done():
    pass

