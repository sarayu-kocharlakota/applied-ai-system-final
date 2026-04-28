## Title and Summary
PawPal+ - Applied AI Pet Care System

The Applied AI Pawpal+ is a pet care app that helps busy owners stay on top of their pet's daily needs. It allows them to add tasks such as walks, medications, feedings, and then uses Claude AI to generate a smart daily schedule with explanations. This app is very beneficial because busy pet owners often struggle or forget to stay consistent with pet care. Having an AI generalized personal schedule saves so much time and helps owners provide the proper care that their pets require every day. 

This project is an extension of the original PawPal+ project from Module 3. The original app allowed pet owners to manually input tasks such as walks, medications, and feedings. It was able to sort tasks by time or priority, detect scheduling conflicts, and support recurring daily or weekly tasks. There was no AI involved at all. All of this was done by using rule-based logic. 

## Architecture Overview 

First, the user enters pet tasks and information into the Streamlit app. The Scheduler then sorts the tasks and detects any conflicts. Next, the AI Scheduler sends those tasks to the Claude API, which returns an intelligent personalized plan which gets displayed back to the user in the app. 

![Architecture Diagram](assets/architecture.png)

## Setup Instruction
1. Clone the repo - Download the project files to your computer
git clone https://github.com/sarayu-kocharlakota/applied-ai-system-final.git
cd applied-ai-system-final

2. Create and activate a virtual environment 
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies - Installs Streamlit and Anthropic
pip install streamlit anthropic

4. Set the API key - Get the key from console.anthropic.com
export ANTHROPIC_API_KEY="your-api-key-here"

5. Run the app - Start the Streamlit app and it opens in browser
streamlit run app.py

## Sample Interactions

**Example 1**
- Pet: Mochi (dog)
- Tasks: Morning walk at 8am (priority 1), Feeding at 9am (priority 2), Medicine at 10am (priority 1)
- AI Output: 
Mochi's Task Plan for Today 🐕
Best Order to Complete Tasks
Morning walk at 8:00 AM (Priority 1)
Feeding at 9:00 AM (Priority 2)
Medicine at 10:00 AM (Priority 1)
Why this works: This order is already ideal! Walking first lets Mochi burn energy and go potty. Feeding after exercise (with a 1-hour gap) allows time for their heart rate to settle, reducing bloat risk. Medicine last ensures it can be given with or after food if needed for absorption or to prevent stomach upset.

Potential Issues 🚩
All clear! The 1-hour gaps between tasks are healthy spacing.
Just confirm whether Mochi's medicine should be taken with food, after food, or on an empty stomach—adjust timing if needed.
Bonus Wellbeing Tip 💡
Since Mochi has medicine scheduled, offer a small treat or extra cuddles afterward as positive reinforcement! This helps reduce any stress around medication time and keeps the experience pleasant for future doses.

Have a wonderful day with Mochi! 🐾

**Example2**
- Pet: Luna (cat)
- Tasks: Two walks scheduled at the same hour being priorities 1 and 2.
- AI Output: 
Luna's Task Review 🐱
1. Best Order for Tasks
Since both tasks are scheduled at the same time (8:00 AM), I'd recommend completing the Morning walk first (priority 1), as it has the higher priority ranking.

2. ⚠️ Potential Issues Flagged
Scheduling conflict! Both walks are set for 8:00 AM — this appears to be a data entry error. You'll want to reschedule the "Afternoon walk" to an actual afternoon time (perhaps 2:00 PM or 4:00 PM).

Cats and walks: Just a gentle note — most cats don't need walks like dogs do! If Luna is harness-trained and enjoys outdoor adventures, that's wonderful. But if not, you might consider replacing "walks" with play sessions instead.

3. 🌟 Bonus Wellbeing Tip
Give Luna some vertical space today! Cats love to climb and perch up high — it helps them feel safe and mentally stimulated. A cat tree, shelf, or even a cleared spot on a bookcase can make her day extra enriching.

Would you like help adjusting Luna's schedule or converting these to indoor play activities? 🐾


## Design Decisions

I chose Claude AI because it has the capability to explain decisions in a simple manner. However, a tradeoff is that it requires an API key and credits to properly function. Streamlit was used for the UI because it's very easy to build an app on with it without needing a separate frontend framework. A tradeoff for this is that, it's a little less customizable than a full web application. Error handling and logging were added so that API failures are carefully tracked and the app never silently crashes, though it adds extra code to maintain. 

## Testing Summary 
All 6 out of 6 tests passed. The tests included task completion, sorting, conflict detection, recurring tasks, and AI error handling. Logging was added to track API requests and failures. The biggest challenge to navigate was definitely setting up the virtual environment and API key properly.  

## Reflection 
This project taught me a lot about AI usage. I learned that although AI can be of great support for projects like this, at the end of the day, it's up to me whether or not I should take its advice and suggestions. I also learned that AI works best only when I give it a clear and specific prompt, rather than a vague one. The biggest challenge I faced when creating this project was getting the anthropic module installed correctly and setting up the API key in the right terminal window every single time. AI helped me learn that errors are more than normal and it's just part of the process of creating something big in the end. It also taught me that certain tools need to be correctly set up in order to work, such as virtual environment and API key. 

## Portfolio Reflection

Creating this project was a great experience. I gained deep knowledge and experience on how to take a simple project and make it more advanced and smart with AI. The thing I felt was most interesting to learn was how to integrate real APIs into working apps. Furthermore, adding error handling so the app displays a kind message rather than crashing when something goes wrong. Also, adding logging allows one to see exactly what the app is doing while it runs. Adding all of these features made me a better AI engineer because I realized that building a proper app is not only about making it work, but also making it very reliable and trustworthy for people to use. I now understand how to integrate APIs, handle errors gracefully, and write tests to check if my code works. Building this app taught me how to expand my thinking beyond just functionality but also to think about considering what happens when things go wrong. 

## GitHub Repository
https://github.com/sarayu-kocharlakota/applied-ai-system-final