# CS Event Generator(CSEG)

the CSEG app is used to generate telemetry for charging stations based on profiles
and specs.

## CSEG API

### setup

#### Request

POST /generate

```json
{
  "coordinates": [
    ["lat", "long"],
    ["lat", "long"],
    ["lat", "long"],
    ["lat", "long"]
  ],
  "date_range": ["start_date", "end_date"]
}
```

#### Response

```json
{
  "id": "uuid",
  "setup": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {
          "population": 200
        },
        "geometry": {
          "type": "Point",
          "coordinates": [-112.0372, 46.608058]
        }
      }
    ]
  }
}
```

### telemetry

#### Request

GET /jobs/{job_id}/telemetry

#### Response

```json
{
  "cs_list": [{ "id": "uuid", "timestamp": "datetime", "powerConsumption": 0 }]
}
```

## Profiles

- read profile
- choose random profile ?

## The Algo

Generator API is started with a config file
pointing to:

- a profile file or several ?
- a list of charging stations

API available

request made to setup ep with:

- coordinates
- dates

respond with:

- a job id
- cs setup

loads the CS related to the coordinates
clock configured with the daterange

creates each CS entity with:

- clock
- profile:
  - selected at random ?
  - always the same ?

The telemetry part:

once all the CS are populated and attached to the generator
-> run the generator
-> merge the telemetry of all entities
-> package the response
-> ready for telemetry call

request made to telemetry ep with:

- an id

respond with:

- batch telemetry

alternative for the telemetry, the request could be a POST with a webhook
and CSEG would upload the batch result with the webhook

## Misc

- logs
