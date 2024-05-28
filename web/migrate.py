from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from shopping import create_app
from common.models import db

app = create_app('develop')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('makemigrations', MigrateCommand)

if __name__ == '__main__':
    manager.run()

