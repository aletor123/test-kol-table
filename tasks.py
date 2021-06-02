from invoke import task

run_with_manage = 'python manage.py'


@task(name='webpack')
def start_webpack(c, mode='development'):
    c.run(f'webpack --config webpack.config.local.js --watch --mode={mode}')


@task
def migrate(c):
    c.run(f'{run_with_manage} makemigrations')
    c.run(f'{run_with_manage} migrate')


@task(name='prepare')
def prepare_backend(c, fill_db=False):
    migrate(c)
    if fill_db:
        c.run(f'{run_with_manage} runscript fill_db')
        print('Database filled')


@task(name='backend')
def start_backend(c):
    c.run(f"{run_with_manage} runserver")
