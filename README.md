# Bob Ross ETL

## Project Summary

Your local public broadcasting station has an overwhelming amount of requests for information on The Joy of Painting with Bob Ross. Their viewers want a website that allows them to filter the 403 episodes based on the following criteria:

- Month of original broadcast
	- This will be useful for viewers who wish to watch episodes that were painted during that same month of the year
- Subject Matter
	- This will be useful for viewers who wish to watch specific items get painted
- Color Palette
	- This will be useful for viewers who wish to watch specific colors being used in a painting

Your local broadcasting station has already done some leg work to gather data. However, it is spread out across multiple different files and formats, which makes the data unusable in its current form. They've already hired another team to build a front-end to allow their viewers to filter episodes of The Joy of Painting and now they've hired you to help them with the process of designing and building a database that will house this collected data in a way that is usable and also build an API to access it.

The data has been collected from numerous sources and is everything required to create a database and API that would allow your local public broadcasting station to provide a service to filter episodes of The Joy Of Painting. Though this data is great, it was collected by three different individuals and they had three different ways they chose to store data. Please review the collected data and design a database that will store all of this information in a way that will make it usable via the API to filter episodes of The Joy of Painting.

Once you have a database designed that will make the collected data usable, it's time to get that data into your database. The data collected is currently in three different sources and none of them will perfectly align to your database structure. You'll need to write some custom code to extract this data from the different files, transform them a bit to make sure they will be able to be stored in our database, and then ultimately load them into it for long-term storage and use by your local public broadcasting station's audience.

The last step is to build an API that utilizes this data. You must build an API that handles filtering so that the 403 episodes can be pared down to the desired episodes to watch. Multiple filters should be usable at the same time and filters should allow the user to select multiple items. For example, viewers should be able to filter by multiple colors.

Your API must:
- Run locally and communicate with your database to get data to the user
- Accept parameters via the URL, query parameters, or even as POST data in the body
- Return JSON with a list of episode information

## Directions

### 1. Install requirements with:
```
pip3 install -r requirements.txt
```

This should install all dependencies.

### 2. Clean up resources/data.txt file with:
```
python3 utils/replace.py
```

This is because data.txt's only relevant separator data is '" (' while Pandas read_csv does not allow for '(' as a separator. It's probably completely doable to do this in the same step/file as ETL.

### 3. Run application with:
```
uvicorn app:app --reload
```

This will host the data on http://localhost:8000/ including creating or connecting to the bob_ross.db database. Note that there is no front end added, so the API itself is located at http://localhost:8000/api/v1/episodes and its related endpoints.

### 4. If no data in database, load resource files by running ETL/ETL.ipynb file

If new data has been added to the database, default behavior is to "replace" data in database. Data can be appended to existing data, but note that current Episode table model does not allow for duplicate data.
