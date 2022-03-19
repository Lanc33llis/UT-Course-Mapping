# UT Course Mapping Bot

## To get started

Windows
```bash
# make a new virtual environment 
python -m venv venv
# activate the virtual environment
.\venv\Scripts\activate
# install the dependencies
pip install -r requirements.txt
# run the bot
python scraper.py -e eid -p password
# caches eid and password so that you may run the bot again without having to enter them
python scraper.py
```

Mac & Linux

```bash
# make a new virtual environment 
python3 -m venv venv
# activate the virtual environment
source python3-virtualenv/bin/activate
# install the dependencies
pip3 install -r requirements.txt
# run the bot
python scraper.py eid password
```