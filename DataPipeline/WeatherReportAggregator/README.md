# WetherReportGenerator



# How to Run Test cases
* Create a virtual environment: `virtualenv pyspark-venv`
* Activate the virtual environment: `source pyspark-ven/bin/activate`
* Install the test's dependency: `pip install -r test_requirements.txt`
* Run the test: `pytest`
In order to generate the unit test report in junit xml and coverage report in Cobetura xml format:
`py.test --cov-report xml:./reports/coverage.xml 
         ----junitxml=./reports/unit-test.xml`
