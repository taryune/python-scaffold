import invoke


@invoke.task
def setup(c):
    invoke.run("pipenv install --dev")
    invoke.run("pipenv run pre-commit install")
