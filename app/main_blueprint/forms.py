from wtforms import Form, StringField, TextAreaField


class KeepForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
