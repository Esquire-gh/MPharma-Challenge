# mPharma Challenge 
This repository contains code for an mPharma coding interview problem

## Requirements
1. Python (Django, DjangoRestFramework)
3. Docker, docker-compose

## Setup & Run
1. Clone repository
2. create an environment variable name `.env`. use the env.sample file as an example
3. build docker images with docker-compose up
4. run the app by using the command `docker-compose up`. Test Endpoint at `localhost:8000`

## Testing API
### Automated Test
Run the command `python -m unittest` from the app's root directory(where you have the manage.py file).

### Manual Test
The API has two endpoints that support the following operations
#### 1. Create a new diagnosis code record
- /POST  /api/v1/codes

data = {
    "category_code": "A00",
    "diagnosis_code": 233,
    "full_code": "A00233",
    "abbreviated_description": "abbrev desc",
    "full_description": "Cholera from Postman and malaria",
    "category_title": "Cholera"
}

NB: `category_code` must be valid

#### 2. Edit an existing diagnosis code record
- /PUT  /api/v1/codes

#### 3. List diagnosis codes with pagination. PAGE_SIZE = 10
- /GET  /api/v1/codes

#### 4. Retrieve diagnosis codes by ID
- /GET  /api/v1/codes/< pk >

#### 5. Delete a diagnosis code by ID
- /DELETE  /api/v1/codes/< pk >


## Architectural Considerations


