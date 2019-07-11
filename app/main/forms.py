from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class BookmeetingForm(FlaskForm):
    title=StringField('Meeting title',validators=[DataRequired()])
    rooms=SelectField('Choose room',coerce=int,choices=RoomChoiceIterable())
    date=DateField('Choose date', format="%m/%d/%Y",validators=[DataRequired()])
    startTime=SelectField('Choose starting time(in 24hr expression)',coerce=int,choices=[(i,i) for i in range(9,19)])
    duration=SelectField('Choose duration of the meeting(in hours)',coerce=int,choices=[(i,i) for i in range(1,6)])
    participants_user=SelectMultipleField('Choose participants from company',coerce=int,choices=UserChoiceIterable(),option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False),validators=[DataRequired()])
    participants_partner=SelectMultipleField('Choose participants from partners',coerce=int,choices=PartnerChoiceIterable(),option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))
    submit=SubmitField('Book')

    def validate_title(self,title):
        meeting=Meeting.query.filter_by(title=self.title.data).first()
        if meeting is not None: # username exist
            raise ValidationError('Please use another meeting title.')

    def validate_date(self,date):
        if self.date.data<datetime.datetime.now().date():
            raise ValidationError('You can only book for day after today.')
