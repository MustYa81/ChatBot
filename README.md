# [WiSe25-26] ChatBot-Projekt 
# Group 23

A chatbot application developed as part of the first-semester project in the DigiTec program. The chatbot can answer questions, provide weather information, compare temperatures, and even play a trivia game.

## 🎯 Purpose

This project is a chatbot application designed to:

- Answer a variety of questions, including banking-related queries and weather information.
- Fetch and display weather information for specific locations using the OpenWeatherMap API.
- Compare local temperature data logged using a Sense HAT with weather forecasts.
- Play a fun trivia game.
- Log errors and user interactions for debugging and monitoring purposes.


## 📦 Installation & Setup

### Prerequisites
- Python 3.12.2 or pythton 3.x
- Sense HAT
- OpenWeatherMap API key
- Virtual environment venv

### Installation Steps

Chatbot Interaction
Run the Chatbot application using this line of command: "python main.py"
Ask questions directly to the chatbot.
Ask the chatbot compound questions.
Use the --show option to list all available questions.
Add or remove questions using the --add and --remove options.
Play the trivia game by typing "trivia".
Weather Information
Ask the chatbot about the weather in a specific location while running the application:

For example: "What is the weather in Wolfenbüttel?"

Add and remove Questions/Answers.
Adding a question with the answer:

python main.py --add --q "Question" --answer "Answer"
Adding another answer to an existing question:

python main.py --add --q "Existing question" --answer "New answer"
Remove a specified answer from a question:

python main.py --remove --q "Existing question" --answer "Specified answer"
Remove an entire Question:

python main.py --remove --q "Existing question"
List all questions
To list all questions:

Python main.py --show "show all questions"
Web Scrapping
To scrape a specified website, you should run this line of command:

Python main.py --scrape "url"
Graphical user interface
To run the application using the GUI:

python "graphical_user_interface.py"

## Logging

Logs are stored in app.log for debugging and monitoring.

## 📄 License

This project is not licensed; it is made for educational purposes to prepare a Chatbot with different features.

## 🆘 Support

For questions about the application or testing scenarios:
- Check the testing notes in each component
- Review the intentional flaws documentation
- Use browser DevTools for debugging
- Test with different browsers and devices

---
