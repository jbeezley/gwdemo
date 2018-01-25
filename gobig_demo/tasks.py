from girder_worker.app import app
from girder_worker_utils import types
from girder_worker_utils.decorators import argument


@app.task
@argument('name', types.String, help="Your pet's name")
@argument('age', types.Integer, min=1, max=20,
          help='An integer between 1 and 20')
@argument('animal', types.StringChoice, choices=['cat', 'dog', 'monkey'])
def add_pet(name, age, animal='dog'):
    """Demo of a task with several different argument types."""
    print('You have a %d year old %s named %s' % (age, animal, name))


@app.task
@argument('guess', types.Range, min=1, max=20,
          help="Pick a number between 1 and 20 (hint: it's 4)")
def guess_a_number(guess=1):
    """Try to guess the number I picked."""
    if guess != 4:
        raise Exception('WRONG!')

    print('You guessed correctly!')
