import click
from lovewall import app, db
from lovewall.models import Message


@app.cli.command()
@click.option('--count', default=20, help='消息数量默认是20条')
def forge(count):
    """创建虚拟数据"""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('工作中。。。')

    for i in range(count):
        message = Message(
            name = fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('创建%d条虚拟数据。' % count)



