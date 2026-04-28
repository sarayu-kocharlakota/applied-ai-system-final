# Model Card — Applied AI PawPal+

## Limitations and Biases

Claude is only aware of the tasks you provide, it doesn't have real knowledge about your specific pet's personality or health history. Therefore, it can only give generic advice, not information that fits every breed or species. 

## Misuse

One could use this app to generate incorrect or harmful care schedule if they put in fake information. A method to prevent this, is the app could add input validation to verify that the tasks and corresponding times are realistic. Furthermore, this could include a disclaimer reminding users that AI suggestions are absolutely not a substitute for professional pet advice. 

## Surprises During Testing

The biggest surprise to me when creating this project was how confusing the system was to setup issues. For example, something as simple as the API key not being set in the right terminal window which caused the entire AI feature to fail. It was also shocking to see Claude respond so accurately and straight to the point when given clear and specific task information. 

## AI Collaboration

A very helpful moment when AI helped me out was when it provided guidance on how to structure the ai_scheduler.py file and suggesting how to handle errors so gracefully. One area where I felt there was a flawed moment was when AI kept giving me incorrect installation commands, which caused a "ModuleNotFoundError" that took so long to fix. 

## Future Improvements

In the future, I want to make this project more advanced so that it can handle multiple pets at once. I also want to add a confidence score so users are aware of how much they can trust Claude  about its suggestions. 
