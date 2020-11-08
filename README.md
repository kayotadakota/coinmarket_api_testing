## Getting started
Clone the repo and go to the directory
```
git clone https://github.com/kayotadakota/coinmarket_api_testing.git
cd coinmarket_api_testing
```
Set virtual environment
```
python -m venv env
```
Activate it
```
env\Scripts\activate
```
Install requirements
```
pip install -r requirements.txt
```
## Running tests
To run all existing tests in the current directory
```
pytest
```
To run a certain test 
```
pytest test_sample.py
```
