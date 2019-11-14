from datetime import datetime
from todo import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	description = db.Column(db.Text)
	date_posted = db.Column(db.DateTime, default=datetime.today().date())
	date_due = db.Column(db.DateTime)
	time = db.Column(db.Time)
	complete = db.Column(db.Boolean, default=False, nullable=False)


	def __repr__(self):
		return "Task('{}', {})".format(self.title, self.complete)

db.create_all()