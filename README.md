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
5. run `docker exec -i <web container name> python manage.py shell < scripts/populate_categories.py` to add the first 100 categories in `diagnosis_codes/data/categories.csv` to the databse

## Testing API
### Automated Test
After starting the application:
- Run the command `docker-compose run web bash ./scripts/run_tests.sh` from the app's root directory(where you have the manage.py file).

### Manual Test
The API has two endpoints that support the following operations
#### 1. Create a new diagnosis code record
- /POST  /api/v1/codes

```
sample_data = {
    "version": "ICD-10-2018",
    "category_code": "A00",
    "diagnosis_code": 233,
    "full_code": "A11233",
    "abbreviated_description": "fasdf",
    "full_description": "This is malaria",
    "category_title": "Cholera"
}
```

NB: `category_code` and `category_title` must be valid

#### 2. List diagnosis codes with pagination. PAGE_SIZE = 20
- /GET  /api/v1/codes


#### 3. Edit an existing diagnosis code record
- /PUT  /api/v1/codes/< pk >


#### 4. Retrieve diagnosis codes by ID
- /GET  /api/v1/codes/< pk >


#### 5. Delete a diagnosis code by ID
- /DELETE  /api/v1/codes/< pk >



## Architectural Considerations
This section explains some of the arhitectural decisions made for this project
#### 1. Models
- The Schema for diagnosis codes has been separated into two models; `Category` and `DiagnosisCode`. 
- This decision is mainly to facilitate backward incompatibility of diagnosis codes and also ensure normalization of data.
- The `Category` model contains all the category codes for for a specific version of diagnosis codes. 
- The decision to use `choices` to store the different version is to avoid making an extra query to retrieve the version of a 
Category. Currently only the `ICD-10-2018` version is supported.
