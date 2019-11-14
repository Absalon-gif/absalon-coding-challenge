from flask import render_template, flash, redirect, url_for, request, jsonify
from todo import app, db
from todo.forms import NewtaskForm
from todo.models import Task



@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
	tasks = Task.query.filter_by(complete = False)
	return render_template('home.html', title='home', tasks=tasks)

@app.route("/task/new", methods=['GET', 'POST'])
def New_tasks():
	form = NewtaskForm()
	if form.validate_on_submit():
		task = Task(title=form.title.data, description=form.description.data, date_posted=form.date_posted.data, date_due=form.date_due.data, time=form.time.data)
		db.session.add(task)
		db.session.commit()
		flash('Your task has been created', 'success')
		return redirect(url_for('home'))
	return render_template('create.html', title='New Task', form=form, legend='New Task')


@app.route("/task/completed", methods=['GET'])
def Completed_tasks():
	tasks = Task.query.filter_by(complete = True)
	return render_template('completed-tasks.html', title='Complete tasks', tasks=tasks)


@app.route("/task/completed/<int:task_id>/remove", methods=['GET', 'POST'])
def removed_task(task_id):
	task = Task.query.get(task_id)
	db.session.delete(task)
	db.session.commit()
	flash("Completed task has been removed!", 'success')
	return redirect(url_for('Completed_tasks'))


@app.route("/task/<int:task_id>")
def task(task_id):
	task = Task.query.get_or_404(task_id)
	return render_template('task.html', title=task.title, task=task)


@app.route("/task/<int:task_id>/edit", methods=['GET', 'POST'])
def update_task(task_id):
	task = Task.query.get_or_404(task_id)
	form = NewtaskForm()
	if form.validate_on_submit():
		 task.title = form.title.data
		 task.description = form.description.data
		 task.date_posted = form.date_posted.data
		 task.date_due = form.date_due.data
		 task.time = form.time.data
		 db.session.commit()
		 flash('Your task has been updated!', 'success')
		 return redirect(url_for('task', task_id=task.id))
	elif request.method == 'GET':
		form.title.data = task.title
		form.description.data = task.description
		form.date_posted.data = task.date_posted
		form.date_due.data = task.date_due
		form.time.data = task.time
	return render_template('create.html', title='Edit Task', form=form, legend='Edit Task')


@app.route("/task/<int:task_id>/delete", methods=['POST'])
def delete_task(task_id):
	task = Task.query.get_or_404(task_id)
	db.session.delete(task)
	db.session.commit()
	flash('Your task has been removed!', 'success')
	return redirect(url_for('home'))


@app.route("/task/<int:task_id>/completed", methods=['POST'])
def task_complete(task_id):
	task = Task.query.get_or_404(task_id)
	task.complete = True
	db.session.add(task)
	db.session.commit()
	flash('Your task has been completed', 'success')
	return redirect(url_for('Completed_tasks'))
	




