# TestTask_fastapi

## Start project

#### Clone repository

`git clone https://github.com/Kap1ch/TestTask_fastapi.git`

#### Create new environment

`python -m venv venv `

#### activate environment

On Windows

`venv\Scripts\activate`

MacOS & Linux

`source venv/bin/activate`

#### Install packages

`pip install -r requirements.txt`

#### Run the application

`uvicorn main:app --reload`

#### Test the endpoint

Send a POST request to `http://127.0.0.1:8000/summarize` with a JSON body containing the text to be summarized.


