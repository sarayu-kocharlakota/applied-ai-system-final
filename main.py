from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

owner = Owner(name="Mandy", email="mandy@gmail.com")
buddy = Pet(name="Leo", species="dog", breed="Labrador", age=6, owner=owner)
whiskers = Pet(name="Coco", species="cat", breed="Siamese", age=7, owner=owner)
owner.add_pet(buddy)
owner.add_pet(whiskers)

task1 = Task(
    title="Breakfast",
    task_type="eating",
    due_datetime=datetime.now().replace(hour=8, minute=0, second=0),
    priority=1,
    pet=buddy
)

task2 = Task(
    title="Morning Walk",
    task_type="walking",
    due_datetime=datetime.now().replace(hour=9, minute=0, second=0),
    priority=2,
    pet=whiskers
)

task3 = Task(
    title="Medication",
    task_type="medication",
    due_datetime=datetime.now().replace(hour=10, minute=0, second=0),
    priority=3,
    pet=whiskers
)

buddy.add_task(task1)
whiskers.add_task(task2)
whiskers.add_task(task3)

scheduler = Scheduler()
scheduler.add_owner(owner)
scheduler.add_task(task1)
scheduler.add_task(task2)
scheduler.add_task(task3)

print("=" * 40)
print("TODAY'S SCHEDULE")
print("=" * 40)
for task in scheduler.sort_by_priority():
    print(f"\nPet: {task.pet.name}")
    print(f"  {task}" )
print("\n" + "=" * 40)
