from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    title: str
    task_type: str
    due_datetime: datetime
    priority: int
    pet: object
    is_complete: bool = False

    def complete(self):
        """Mark this task as complete."""
        self.is_complete = True

    def is_overdue(self) -> bool:
        """Return True if the task is past its due time and not complete."""
        return not self.is_complete and datetime.now() > self.due_datetime

    def __str__(self):
        """Return a formatted string representation of the task."""
        status = "✅" if self.is_complete else "❌"
        overdue = " (OVERDUE)" if self.is_overdue() else ""
        return f"{status} [{self.task_type.upper()}] {self.title} - Due: {self.due_datetime.strftime('%I:%M %p')}{overdue} (Priority: {self.priority})"


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    owner: object
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks

    def __str__(self):
        """Return a formatted string representation of the pet."""
        return f"{self.name} ({self.species}, {self.breed}, age {self.age})"


@dataclass
class Owner:
    name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Register a new pet under this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str):
        """Remove a pet by name from the owner's list."""
        self.pets = [p for p in self.pets if p.name != pet_name]

    def get_pets(self) -> List[Pet]:
        """Return all pets belonging to this owner."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all of this owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    def __init__(self):
        """Initialize the scheduler with empty task and owner lists."""
        self.tasks: List[Task] = []
        self.owners: List[Owner] = []

    def add_owner(self, owner: Owner):
        """Add an owner to the scheduler."""
        self.owners.append(owner)

    def add_task(self, task: Task):
        """Add a task to the scheduler's task list."""
        self.tasks.append(task)

    def get_todays_tasks(self) -> List[Task]:
        """Return all tasks that are due today."""
        today = datetime.now().date()
        return [t for t in self.tasks if t.due_datetime.date() == today]

    def sort_by_priority(self) -> List[Task]:
        """Return tasks sorted by priority, lowest number first."""
        return sorted(self.tasks, key=lambda t: t.priority)

    def detect_conflicts(self) -> List[tuple]:
        """Detect and return pairs of tasks that overlap for the same pet."""
        conflicts = []
        tasks = self.sort_by_priority()
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                t1, t2 = tasks[i], tasks[j]
                if t1.pet == t2.pet and t1.due_datetime == t2.due_datetime:
                    conflicts.append((t1, t2))
        return conflicts