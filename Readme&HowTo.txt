Notes:
- Automation Project is in its Folder.
- Other documents are in the main folder

!BONUS! GitHub Link - https://github.com/dvir-karilker/KaleidooProj/tree/master
(git add .   |  git commit -m "bla bla"    |  git push      (<- already established connection in my VS Code)

TO RUN CODE:
after extracting ALL, navigate to "Automation" folder. Inside, right-click and open the Terminal.
Type in "pytest test_main.py".


Automation:
- Make sure Python ver. is 3.12.2 or higher
- "requirements.txt" file is attached for needed Framework/s / Module/s (Terminal/CMD command " pip install -r requirements.txt ")
- "geckodriver.exe" is attached for local WebDriver support of the Mozilla Firefox Browser.
- Comments, Notes and other Documentation Info will be included in the code as Comments.
- Will use the Login Page URL ("https://homme.co.il/wp-login.php") instead of the main one to shorten the process.





Description:
This Automation Project's purpose is to perform an end-to-end automation test on the "Publish Ad" (פרסום מודעה) Page's functionality.
The Test will be divided to "mini-tests", using a created Class' Methods, to adjust Selenium's methods to be reused and for different scenarios, and performed
using the Pytest Framework.

The Test will be performed in the following steps:
1. Navigating to the System.
2. Logging in to the System using the credentials provided to me.
3. Creating a New Listing (only Valid/Positive scenario is tested).
4. Checking that the New Listing is created by validating its creation and details in a few places.




Files:
1. main.py - Contains the "Base" class, responsible for constructing the Driver Object, and other Methods which we will use in our Testing.
2. test_main.py - Uses the "Base" class and its Methods to execute the Tests, using the pytest framework.


  