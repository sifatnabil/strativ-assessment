# Should I Travel There?

## Problem Definition

This repo is about a solution for an assessment provided by Strativ. There are coordinates available for 64 districsts of Bangladesh. Using these cooridinates, we can use the open source API from [Open-Meteo](https://open-meteo.com/) to get weather forecast. The idea is to collect next 10 days of foreacast and create a record of top 10 coolest districts. After that, create a query-able API for an user to decided whether he/she should travel to a particular district or not depending on if it's warmer there or not. The user will provide a source district and a destination district. The API will respond according to that using OpenAI API.

## Installation

1. Install the required Packages using the command: `pip install -r requirements.txt`
2. Create a `.env` file in the root directory and add the value for the OpenAI API key:
`OPENAI_API_KEY=<your_api_key>`
3. Create the Database by running the file using the command: `python utils/db.py`
4. Put the coordinates data in the `data` folder
5. Gather the weather data and insert it in the database usign the command: `python utils/weather.py`
6. Run the application using the command: `uvicorn app.main:app --relaod`

The API documentation is available at: `/api/docs`.

## Contact

Feel free to contact me for any feedback, suggestion or collaboration.

- **Email**: _[sifatnabil@gmail.com](mailto:sifatnabil@gmail.com)_
- **LinkedIn**: _[linkedin.com/in/sifatnabil](https://www.linkedin.com/in/sifatnabil/)
