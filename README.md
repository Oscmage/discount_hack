# Discount service

This is a draft of a python discount service providing a brand with the possibility to generate codes to be used for discounts.

The service make use of [FastAPI](https://fastapi.tiangolo.com/). 

For testing [pytest](https://docs.pytest.org/en/6.2.x/) is used.

## Documentation
The API documentation for the Service can be found by running the service (see setup) and by going to the following address:

```
http://127.0.0.1:8000/docs
```
It is very much in a draft stage.

### Ubiquitous language

#### Brand
A brand is a company selling something on our platform. Example of brands are Nike, Adidas etc.

#### Code
A "code" is a string that can be used by a customer for retrieving different type of discounts.

#### Batch
An overarching object for a set of codes with the same business rules. 
A batch is connected to a brand.   
 
#### Price rule
A price rule is a concept of specifying rules for a batch and related codes. 
For example, it could contain restrictions on how many times a code can be used,
whether the code applies to all line items or percentage of the full order etc.

## Setup

1. Make sure you have Python installed.
2. Create a new virtualenv (https://github.com/pyenv/pyenv-virtualenv)
3. Assuming you have pyenv virtualenv available:
```sh
# Install Python version
pyenv install 3.9.5

# Create a new virtualenv called 'discount'
pyenv virtualenv 3.9.5 discount

# Activate the new virtualenv
pyenv activate discount

# Install the requirements necessary to run the project. 
# Eventually we want to split the testing dependencies and the production running once, 
# due to the limit of time that is not the case. 
pip install -r requirements.txt
```
4. Try running the tests by going into the root directory and running
```sh
pytest
```

5. Start the application in development mode by going into the root directory and run:
```sh
uvicorn main:start --reload
```

6. Try hitting the API (See documentation `http://127.0.0.1:8000/docs` for more information)
```sh
curl --location --request POST 'http://127.0.0.1:8000/v1/create_batch/100/608480c4-d8b1-48e1-8039-33df4f356126/608480c4-d8b1-48e1-8039-33df4f356125'
```
(For now any price_rule_ref and brand_ref works as long as they are uuids)

7. Retrieve a code for a batch created (using the batch_ref from step 6.)
```sh
curl --location --request GET 'http://127.0.0.1:8000/v1/retrieve_code/2f0811cb-b102-4263-b355-78bf95eaa2f5/2f0811cb-b102-4263-b355-78bf95eaa2f4'
```

## Appendix

Intended long term design can be found under `design_draft.jpeg`. 
This service is written in Python as an experiment while the design mentions Golang which is more appropriate when it comes to scalability.



