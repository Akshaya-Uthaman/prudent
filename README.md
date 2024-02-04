# Installations
 * Create a pipenv
 * Install all dependencies present in the file 'requirements.txt' using the command ' pip install -r requirements.txt '
 * To see reporting, install allure using the command ' scoop install allure '

# Executing/Running
* To run the file with allure reporting, use command ' pytest step_defs/test_search_api.py  --alluredir=./allure-results ' or ' pytest step_defs  --alluredir=./allure-results '
* To generate allure report, use command ' allure generate ./allure-results --clean -o ./allure-report '
* To open allure reports, use command ' allure open ./allure-report '
