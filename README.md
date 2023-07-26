# Automatic search and filter test on the Divar site

This test script allows you to perform various actions on the Divar website using Selenium and Python. The implemented tasks include searching for items, applying filters based on color, category, price, and mileage, selecting urgent items, and choosing one of the search results. The project uses the Page Object Model (POM) design pattern for better code organization and maintenance.

**Technologies Used:**

1. Python: The programming language used for implementing and writing the tests.
2. Selenium Framework: A popular tool for automating web browsers, used here to interact with the Divar website.
3. Pytest Framework: Used for better test management and assertions.
4. Logging: For managing and storing logs during test execution.
   Follow the path below to see the logs: src/logs_config/logs.log
5. YAML: For managing input data in a structured way.

**Installation:**

    git clone https://github.com/farzane-shafiee/automate-divar-selenium-python.git

    cd automate-divar-selenium-python
    
    create ENV and active it:

        for win: 
            python -m venv env

        for linux: 
            pip install virtualenv
            virtualenv --python=python3 venv
            source venv/bin/activate

    install dependencies:
        pip install -r requirements.txt

    run tests:
        cd src/
        pytest
