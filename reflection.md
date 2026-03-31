# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My UML design contains four classes. The four classes are: Owner, Pet, Task, and Scheduler. The Owner class' responsibilty is to represent the person using the app and holds the app user's name, email, and a list of their pets. The Pet class represents an animal and holds its species, breed, name, and age. The Task class responsibilty is to hold a care activity such as a walk, medication, feeding, and keeps tabs of the due date, priority, and if it has been completed. The Scheduler class is the main function of the app. It handles every single task and can order them in terms of priority and identify conflicts in scheduling. 

**b. Design changes**

My design changed a bit during implemenation. After referring to AI and asking it if there were any potential missing relationships, I realized that Scheduler had no direct connection to Owner. Therefore, I included an owners list to the Scheduler class. This way, it can keep note of the owners that are in the system. I made this change as now, it would be much more simpler to look up tasks by owner in the future. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The two constraints that my scheduler considers are time (the due date of a task) and priority (how important a task is, 1 being highest). I decided that these two constraints mattered the most as every task for a pet has a specific time it needs to get done. Furthermore, there will always be tasks that are more important to get done than others. 

**b. Tradeoffs**

One tradeoff my scheduler makes is that it only verifies for exact hour matches when analyzing conflicts. If there is one task at 8:00am and another at 8:30am, nothing gets flagged. However, if both tasks are at 8:00am, it gets flagged. This tradeoff is reasonable for this scenario as this is a straightforward and easy app for pet care. So, just checking hours works great. The most common timings for tasks for pets such as feedings or walks are scheduled on the hour. This covers frequently occuring cases which prevents the code from being overly complex. 

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools to help me generate the UML diagram, to help generate the skeleton code, implement the full classes, write tests, and to help solve the bug with the conflict detection. AI is so useful when wanting support in understanding specific parts of a code and debugging issues in the code. The prompts where I ask for guidance in these, are the most beneficial. 

**b. Judgment and verification**

I didn't accept an AI suggestion as-is was when the conflict detection was not properly working. The initial code that the AI provided was not flagging conflicts when it was clearly supposed to. When I ran the script, the output kept displaying "No conflicts detected". This was when I knew that AI was giving me inaccurate suggestions, as there were clearly two tasks at the same exact hour. 
---

## 4. Testing and Verification

**a. What you tested**

I tested these five behaviors: task completion status, adding tasks to pets, sorting tasks by time, recurring task logic, and conflict detection. These tests were very important as they confirmed that the main logic of the scheduler accurately worked before linking it to the UI. 

**b. Confidence**

I am extremely confident that my scheduler works correctly. All five tests passed and everything ran properly with no errors. If given extra time, I would have tested edge cases such as a pet that has no tasks in a day and two different pets with a task at the same hour. 
---

## 5. Reflection

**a. What went well**

The part that I am most satisfied with about this project is the UI working well and properly. 

**b. What you would improve**

If I had another iteration, something I would improve is making the app look nicer. I definitely would have added some nice touches to make it look more appealing.   

**c. Key takeaway**

One important thing I learned about designing systems or working with AI on this project is that yes, of course AI can generate the code you want it to. However, what's more important is that you actually understand and verify it. I realized that although AI can give all the suggestions that it wants to give, it's up to us if we want to take them or not. 
