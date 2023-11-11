from wtforms import Form
from wtforms.fields import (
    HiddenField, StringField, IntegerField, SubmitField, DateField
)

class CreateForm(Form):
  subject = StringField('タスク名')
  deadline = DateField('期限', format='%Y-%m-%d')
  comment = StringField('コメント')
  submit = SubmitField('タスク作成')

class UpdateForm(Form):
  id = HiddenField()
  subject = StringField('タスク名')
  deadline = DateField('期限:', format='%Y-%m-%d')
  comment = StringField('コメント:')
  submit = SubmitField('更新')

class DeleteForm(Form):
  id = HiddenField()
  submit = SubmitField('完了')
