from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def make_owner():
    return Owner(name="Mandy", email="mandy@gmail.com")

def make_pet(owner):
    return Pet(name="Leo", species="dog", breed="Labrador", age=6, owner=owner)

def make_task(pet, hour=8, priority=1, frequency=None):
    return Task(
        title="Test Task",
        task_type="walk",
        due_datetime=datetime.now().replace(hour=hour, minute=0, second=0, microsecond=0),
        priority=priority,
        pet=pet,
        frequency=frequency
    )


def test_task_completion():
    """Task should be marked complete after calling complete()."""
    owner = make_owner()
    pet = make_pet(owner)
    task = make_task(pet)
    assert task.is_complete == False
    task.complete()
    assert task.is_complete == True


def test_task_addition():
    """Adding a task to a pet should increase its task count."""
    owner = make_owner()
    pet = make_pet(owner)
    task = make_task(pet)
    assert len(pet.get_tasks()) == 0
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1


def test_sort_by_time():
    """Tasks should be returned in chronological order."""
    owner = make_owner()
    pet = make_pet(owner)
    task1 = make_task(pet, hour=10)
    task2 = make_task(pet, hour=8)
    task3 = make_task(pet, hour=9)
    scheduler = Scheduler()
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0].due_datetime.hour == 8
    assert sorted_tasks[1].due_datetime.hour == 9
    assert sorted_tasks[2].due_datetime.hour == 10


def test_recurring_task():
    """Marking a daily task complete should create a new task for the next day."""
    owner = make_owner()
    pet = make_pet(owner)
    task = make_task(pet, frequency="daily")
    scheduler = Scheduler()
    scheduler.add_task(task)
    scheduler.mark_task_complete(task)
    assert task.is_complete == True
    assert len(scheduler.tasks) == 2
    new_task = scheduler.tasks[-1]
    assert new_task.due_datetime.date() == (datetime.now() + timedelta(days=1)).date()


def test_conflict_detection():
    """Two tasks at the same hour for the same pet should be flagged as a conflict."""
    owner = make_owner()
    pet = make_pet(owner)
    task1 = make_task(pet, hour=8)
    task2 = make_task(pet, hour=8)
    scheduler = Scheduler()
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1

def test_ai_scheduler_no_tasks():
    """AI scheduler should handle empty task list gracefully."""
    from ai_scheduler import generate_ai_schedule
    result = generate_ai_schedule("Mochi", "dog", [])
    assert "No tasks" in result