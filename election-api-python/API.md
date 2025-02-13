# Election Results API Documentation

## Overview
This is the API documentation for the election results service.

## Version
1.0.0

## Endpoints

### GET /scoreboard
Retrieves the scoreboard of election results, including the number of seats, votes, and vote share for each party, as well as the overall winner if any party has secured the required number of seats.

#### Produces
- The API returns data in JSON format.

#### Responses
- **200 OK**
  - Description: The response is a dictionary containing the election results for each party and the overall winner.
  - Structure:
    - The response is an object with the following properties:
      - **CON**: An object representing the Conservative party's results.
        - **Seats**: The number of seats won by the Conservative party (integer).
        - **Votes**: The number of votes received by the Conservative party (integer).
        - **Share**: The vote share of the Conservative party (number).
      - **LAB**: An object representing the Labour party's results.
        - **Seats**: The number of seats won by the Labour party (integer).
        - **Votes**: The number of votes received by the Labour party (integer).
        - **Share**: The vote share of the Labour party (number).
      - **Winner**: The overall winner of the election (string), or `None` if no party has secured the required number of seats.
    - Note: There are other parties included in the results, but only the two major parties are detailed here.

  - Example:
    ```json
    {
      "LAB": {
        "Seats": 4,
        "Votes": 64906,
        "Share": 0.40372964432778075
      },
      "CON": {
        "Seats": 0,
        "Votes": 36918,
        "Share": 0.22963810756005623
      },
     ... , 
      "Winner": null
    }
    ```