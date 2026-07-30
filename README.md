**WebApplication_Project**

A Selenium automation testing framework developed in Python language using the Page Object Model (POM) design pattern. 
The framework uses  Pytest for test execution and generates HTML reports for test results.

**Project Architecture**

The framework follows the Page Object Model architecture to improve maintainability, readability, and scalability.
Below is the structure of the Project created using POM,

WebApplication_Project/
│
│
|----- Page_locators/
│   		|----Locators.py
│   
|---------Reports/
│		|── Homepage_Report.html
│   		|── ValidLogin_Report.html
│   		|── InvalidLogin_Report.html
│   		|── Logout_Report.html
│   		|── UI_Report.html
│   		└── Chatbox_Report.html
│
|------test_validation/
│   		|── __init__.py
│   		|── test_validlogin_verification.py
│   		|── test_invalidLogin_validation.py
│   		|── test_homepage_menu_validation.py
│   		|── test_logout_validation.py
│   		|── test_UI_validation.py
│  		└── test_Dobby_Assistant_validation.py
│
|------ conftest.py
|------ main.py
└── README.md



**Framework Design**

The framework is divided into multiple layers based on the functionality of POM

**Page Object Layer**

Contains all web element locators and reusable page methods.

Responsibilities:

- Store element locators
- Perform UI interactions
- Encapsulate page-specific functionality

Location:
Page_locators/

**Test Layer**

Contains all test cases to be executed.

Responsibilities:

- Execute test scenarios
- Validate expected behaviour
- Call methods from Page Objects

Location:
test_validation/

**Configuration Layer**

`conftest.py`

Responsibilities:

- Browser initialization
- Driver setup
- Fixtures


**Report Layer**

Stores generated HTML reports after execution for each test cases executed in the project with test result.

Location:
Reports/

**Features**

- Selenium WebDriver automation
- Page Object Model architecture
- Pytest test framework
- HTML Test Reports
- Reusable page methods
- Browser fixture management
- Easy maintenance
- Scalable automation framework

**Test Scenarios Covered**

Login Validation

- Valid Login
- Invalid Login


Homepage Validation

- Homepage menu verification
- Navigation validation


Logout Validation

- Logout functionality


UI Validation

- UI element visibility
- Page component verification

Chatbox / Dobby Assistant Validation

- Assistant launch
- Chat window validation
- User interaction

**Prerequisites**

- Python 3.10+
- Google Chrome
- ChromeDriver
- pip

**Required Python Packages**

Install dependencies:

pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager

**Generate HTML report**


pytest <test Name>--html=Reports/Test_Report.html

**Reports**

Generated reports are stored in:
Reports/

Reports generated are:

- Homepage_Report.html
- ValidLogin_Report.html
- InvalidLogin_Report.html
- Logout_Report.html
- UI_Report.html
- Chatbox_Report.html


