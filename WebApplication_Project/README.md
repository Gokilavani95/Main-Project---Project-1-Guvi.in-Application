# WebApplication_Project

A Selenium automation testing framework developed in **Python** using the **Page Object Model (POM)** design pattern.

The framework uses **Pytest** for test execution and generates **HTML reports** for test results.

---

# Project Architecture

The framework follows the **Page Object Model (POM)** architecture to improve maintainability, readability, and scalability.

Project structure:

```text
WebApplication_Project/
│
├── Page_locators/
│   └── Locators.py
│
├── Reports/
│   ├── Homepage_Report.html
│   ├── ValidLogin_Report.html
│   ├── InvalidLogin_Report.html
│   ├── Logout_Report.html
│   ├── UI_Report.html
│   └── Chatbox_Report.html
│
├── test_validation/
│   ├── __init__.py
│   ├── test_validlogin_verification.py
│   ├── test_invalidLogin_validation.py
│   ├── test_homepage_menu_validation.py
│   ├── test_logout_validation.py
│   ├── test_UI_validation.py
│   └── test_Dobby_Assistant_validation.py
│
├── conftest.py
├── main.py
└── README.md
```

---

# Framework Design

The framework is divided into multiple layers based on the **Page Object Model (POM)** architecture.

## 1. Page Object Layer

Contains all web element locators and reusable page methods.

### Responsibilities

- Store element locators
- Perform UI interactions
- Encapsulate page-specific functionality

**Location**

```text
Page_locators/
```

---

## 2. Test Layer

Contains all test cases to be executed.

### Responsibilities

- Execute test scenarios
- Validate expected behavior
- Call methods from Page Objects

**Location**

```text
test_validation/
```

---

## 3. Configuration Layer

**File**

```text
conftest.py
```

### Responsibilities

- Browser initialization
- Driver setup
- Pytest fixtures

---

## 4. Report Layer

Stores generated HTML reports after execution for each test case.

**Location**

```text
Reports/
```

---

# Features

- Selenium WebDriver automation
- Page Object Model (POM) architecture
- Pytest testing framework
- HTML test reports
- Reusable page methods
- Browser fixture management
- Easy maintenance
- Scalable automation framework

---

# Test Scenarios Covered

## Login Validation

- ✅ Valid Login
- ✅ Invalid Login

---

## Homepage Validation

- ✅ Homepage menu verification
- ✅ Navigation validation

---

## Logout Validation

- ✅ Logout functionality

---

## UI Validation

- ✅ UI element visibility
- ✅ Page component verification

---

## Chatbox / Dobby Assistant Validation

- ✅ Assistant launch
- ✅ Chat window validation
- ✅ User interaction

---

# Prerequisites

- Python 3.10 or later
- Google Chrome
- ChromeDriver
- pip

---

# Required Python Packages

Install the required dependencies:

```bash
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager
```

Or install them together:

```bash
pip install selenium pytest pytest-html webdriver-manager
```

---

# Generate HTML Report

Run a specific test and generate an HTML report:

```bash
pytest <test_name> --html=Reports/Test_Report.html
```

**Example**

```bash
pytest test_validation/test_validlogin_verification.py --html=Reports/ValidLogin_Report.html
```

---

# Reports

Generated HTML reports are stored in:

```text
Reports/
```

The generated reports include:

- Homepage_Report.html
- ValidLogin_Report.html
- InvalidLogin_Report.html
- Logout_Report.html
- UI_Report.html
- Chatbox_Report.html

---

# Technology Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- ChromeDriver
- pytest-html

---

# Project Highlights

- Organized using the **Page Object Model (POM)** design pattern.
- Reusable page methods improve maintainability.
- Separate layers for locators, tests, configuration, and reports.
- HTML reporting for better test result visualization.
- Easy to extend with additional test cases and page objects.
