from fastapi import FastAPI

from azure_geos import all_regions

app = FastAPI()


@app.get('/azure/regions/geo/')
async def message():
    return all_regions


@app.get('/azure/{region}/geo/')
async def root(region: str, ):
    for i in range(len(all_regions)):
        if all_regions[i]['name'] == region:
            return all_regions[i]



# Path: superfast/main.py