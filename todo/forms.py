from datetime import datetime, time, date
from flask import flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Length, InputRequired


class NewtaskForm(FlaskForm):
	title = StringField('Title of task', validators=[DataRequired(), Length(min=1, max=20)])
	description = TextAreaField('Description', validators=[Length(min=2, max=150)])
	date_posted = DateField('Date posted', default=datetime.today(), validators=[InputRequired()])
	date_due = DateField('Due date', validators=[DataRequired()])
	time = TimeField('Set Timer for:', validators=[DataRequired()], format='%H:%M')
	submit = SubmitField('Add Task')

	def validate(self):
		time_now = datetime.now().time()
		if self.date_posted.data > self.date_due.data:
			return flash('Due date must be after/equal-to Date posted', "error")
		elif self.date_due.data == self.date_posted.data:
			if self.time.data < time_now:
				return flash('Please set time after {} '.format(time_now.strftime('%H:%M')), "error")
			else:
				return True
		elif self.date_due.data > self.date_posted.data:
			return True