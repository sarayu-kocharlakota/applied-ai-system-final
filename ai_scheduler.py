import anthropic
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def generate_ai_schedule(pet_name: str, species: str, tasks: list) -> str:
    """Send tasks to Claude and get back a smart daily schedule with explanations."""
    
    if not tasks:
        logger.warning("No tasks provided to AI scheduler.")
        return "No tasks found. Please add some tasks first!"

    task_list = "\n".join([
        f"- {t.title} at {t.due_datetime.strftime('%I:%M %p')}, priority {t.priority}"
        for t in tasks
    ])

    prompt = f"""You are a helpful pet care assistant. 
A {species} named {pet_name} has the following tasks scheduled today:

{task_list}

Please:
1. Suggest the best order to complete these tasks and why
2. Flag any potential issues (e.g. tasks too close together)
3. Give one bonus tip for {pet_name}'s wellbeing today

Keep your response friendly, clear, and under 200 words."""

    try:
        logger.info(f"Sending {len(tasks)} tasks to Claude for {pet_name}...")
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        logger.info("AI schedule generated successfully.")
        return message.content[0].text
    except Exception as e:
        logger.error(f"AI scheduler error: {e}")
        return f"⚠️ Something went wrong with the AI: {str(e)}"