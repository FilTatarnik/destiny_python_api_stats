# destiny_python_api_stats
# Initial Set up
1. Clone into this Repo
# Bungie.net Side of things
2. Sign up for Bungie.net account
3. Make your way towards the Bungie Developer Portal
4. Create a new Bungie Application
5. Generate an API_KEY
# Inside the Project Folder
6. Make sure you're inside of the main destiny_python_api_stats folder
7. Open the Project with your preferred IDE. Mine's vscode. --> type 'open .' to open the location you're at with vscode through the terminal
8. Inside of the Config.py file add your api_key = 'your_api_key', save
9. Re-Open your terminal
# Installing Dependencies
10. Make sure you have Python installed 'python --version', if not install Python.. https://www.python.org/downloads/
11. Make sure you have Pip installed 'pip --version', if not install Pip.. https://pip.pypa.io/en/stable/installing/
12. Install dependencies, pip install requests
13. cd into destiny_python_backend
# Running the Python File
14. type, destiny_python_api.py to run the Python file
15. In your terminal you should get asked, 'Input your Bungie Acc name: '
16. At the moment it only searches for Steam Users
17. Also, if your name is generic like, 'Leo'. Then it might not be able to bring up your stats becuase there are many 'Leo's out there. 
18. ^there is an endpoint in the API that allows Users to get back an Array of Accounts from a SearchQuery. That's what I'm going to implement next and allow Users to Select their Account based off of their Steam Avatar or something
19. Hit enter
# What to expect
<img src='https://i.imgur.com/hrM9vT9.gif'>
20. Tada! Stats
