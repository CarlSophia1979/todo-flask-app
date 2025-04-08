from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect('/')


#  Make sure this is here!
if __name__ == '__main__':
    app.run(debug=True)
