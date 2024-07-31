# courseRegBot
This is a course registration bot developed to pick and drop courses without incessant user input for hours. This bot uses selenium web driver and operates chrome in a headless mode. It primarily works by using X Path or XML Path Language, and using that, traverses the nodes of a given website, to click on the desired course.

Features

Headless browser automation for efficient operation
Secure login functionality
Persistent automation with error handling and recovery
Custom Browser class for encapsulated web automation functionalities

Prerequisites

Python 3.x
Chrome browser
ChromeDriver compatible with your Chrome version OR if this is being used on Mozilla, then geckodriver.

Installation

Clone this repository:
Copygit clone https://github.com/crypten-glitch/courseRegBot.git
cd course-registration-bot

Install required Python packages:
Copypip install selenium

Download ChromeDriver and place it in the specified path in the script or update the driver_path variable.
Create a secret.py file in the same directory with your login credentials:
pythonCopyusername = "your_username"
password = "your_password"


Usage

Update the driver_path and login_url variables in the script according to the course required.
Run the script:
Copypython main.py

The bot will attempt to log in and register for the course. It will continue running until successful or until manually stopped.

Customization

Modify the XPath selectors in the Browser class methods if the website structure changes.
Adjust the number of registration attempts by changing the range in the click_button_repeatedly method.

Disclaimer
This bot is for educational purposes only. Please ensure you have permission to use automated tools on the target website and comply with all relevant policies and regulations.
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
