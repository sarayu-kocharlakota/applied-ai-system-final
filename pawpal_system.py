"""
pawpal_system.py
PawPal+ backend logic: Owner, Pet, Task, Scheduler
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    title: str
    task_type: str          # e.g. "feeding", "walk", "medication", "appointment"
    due_datetime: datetime
    priority: int           # 1 = highest priority
    pet: object             # reference to Pet (use object to avoid forward-ref issues)
    is_complete: bool = False

    def complete(self):
        """Mark this task as done."""
        pass

    def is_overdue(self) -> bool:
        """Return True if the task is past its due time and not complete."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    owner: object           # reference to Owner
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        pass

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        pass


@dataclass
class Owner:
    name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Register a new pet under this owner."""
        pass

    def remove_pet(self, pet_name: str):
        """Remove a pet by name."""
        pass

    def get_pets(self) -> List[Pet]:
        """Return all pets owned."""
        pass


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the scheduler."""
        pass

    def get_todays_tasks(self) -> List[Task]:
        """Return all tasks due today."""
        pass

    def sort_by_priority(self) -> List[Task]:
        """Return tasks sorted by priority (lowest number = highest priority)."""
        pass

    def detect_conflicts(self) -> List[tuple]:
        """Detect tasks that overlap in time for the same pet."""
        pass