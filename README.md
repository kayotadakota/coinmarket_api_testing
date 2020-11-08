## Getting started
To use coinmarket API you need to have API key. Follow [this guide](https://coinmarketcap.com/api/documentation/v1/#) to get it.
When do you have the key you can do following:
- Change the value of the 'X-CMC_PRO_API_KEY' key manually for all files that contain 'headers'
- Set environment variable

Set environment variable in **Windows**:
- Open System Properties. Just type 'env' in the windows search tab and hit enter
- Open Environment Variables tab
- In User Variables hit New
- Name it whatever you want
- Put your API key into the value box and hit 'ok'
- Ensure you restarted command prompt before testing

Set environment variable in **Linux/Mac**:
```
export NAME=VALUE
```
____

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
