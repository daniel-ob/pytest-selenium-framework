# Pytest Selenium Framework
## Install on virtual environment

```
$ git clone https://github.com/daniel-ob/PytestSeleniumFramework.git
$ cd PytestSeleniumFramework 
$ python3 -m venv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
(env)$ pip install -e .
```
Then configure path to drivers in *tests/conftest.py*

## Launch tests
From PytestSeleniumFramework folder:

### All tests
```
(env)$ pytest --html=reports/report.html
```
### Test subset
```
(env)$ pytest -k {substring_expression} --html=reports/report.html
```

## References

https://www.selenium.dev/documentation/en/

https://docs.pytest.org/en/stable/index.html

https://blog.testproject.io/2019/07/16/develop-page-object-selenium-tests-using-python/

For `pytest_runtest_makereport` hook in *conftest.py*:

https://pytest-html.readthedocs.io/en/latest/user_guide.html

https://github.com/pytest-dev/pytest-html/issues/186#issuecomment-441208344
