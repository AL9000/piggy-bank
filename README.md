# Piggy bank API

## Installation

### Using docker-compose :

Weird "bug" with docker-compose, ot does not wait for the db container to be ready to run the web container ...

So you have to call this command twice:
```shell
docker-compose up
```

You can now access the DRF browsable API directly with your favorite Firefox browser at http://0.0.0.0:8000

### Extras

You can see code coverage after calling `docker-compose up`.

## API docs

You can find documentation about the three actions available directly on the browsable API.

### Shake your piggy bank
Do a GET request to "shake" your piggy bank, it will return your savings amount,
in euros.

### Save money in your piggy bank
Do a PUT request to save some money, just give a positive integer in one of the
following values representing the number of each coin or banknote you are putting
in the piggy bank : cent_one, cent_two, cent_five, cent_ten, cent_twenty,
cent_fifty, euro_one, euro_two, euro_five, euro_ten, euro_twenty, euro_fifty,
euro_hundred, euro_two_hundred, euro_five_hundred

### Break your piggy bank
Do a DELETE request to definitely break your piggy bank and get your money back.
It will return all the coins and banknotes you had put inside.


## Develop on local machine
If you want to dev locally, do the following instructions ;

### Docker image integration
Use the functionalities from your IDE to integrate it with the Dockerfile.

### venv
Or do it with a venv :
- clone this repo
```shell
git clone git@github.com:AL9000/piggy-bank.git
```
- create a virtualenv with python3.11 and activate it
```shell
python3.11 -m venv venv
source venv/bin/activate
```
- install requirements
```shell
python -m pip install requirements.txt
```

### Coverage
- run coverage
```shell
python -m coverage run --source='./savings' manage.py test savings
```
- show coverage report
```shell
python -m coverage report
```
OR
- show coverage report as html
```shell
python -m coverage html
```

# TODOs
- [ ] Make it production ready with docker-compose and PostgreSQL
