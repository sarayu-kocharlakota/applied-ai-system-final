from datetime import datetime
from pawpal_system import Task, Pet, Owner

def test_task_completion():
    owner = Owner(name="Mandy", email="mandy@gmail.com")
    pet = Pet(name="Leo", species="dog", breed="Labrador", age=6, owner=owner)
    task = Task(
        title="Breakfast",
        task_type="eating",
        due_datetime=datetime.now(),
        priority=1,
        pet=pet
    )
    assert task.is_complete == False
    task.complete()
    assert task.is_complete == True

def test_task_addition():
    owner = Owner(name="Mandy", email="mandy@gmail.com")
    pet = Pet(name="Leo", species="dog", breed="Labrador", age=6, owner=owner)
    task = Task(
        title="Morning Walk",
        task_type="walk",
        due_datetime=datetime.now(),
        priority=2,
        pet=pet
    )
    assert len(pet.get_tasks()) == 0
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1