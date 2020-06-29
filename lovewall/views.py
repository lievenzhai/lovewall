from lovewall import app, db
from lovewall.forms import HelloForm
from lovewall.models import Message
from flask import render_template, url_for, flash, redirect


@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    print(messages)
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('你的消息已经发送给世界')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
