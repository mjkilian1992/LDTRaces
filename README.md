# Ticket API - Michael Kilian

## Installation and run instructions
### Pre-requisites
You will need to install the following if you dont have them already:
 + [Poetry](https://python-poetry.org/docs/)
 + Python 3.11.3
   + I highly recommend using [PyEnv](https://github.com/pyenv/pyenv) to get 
     the right version

If you're installing these, I recommend installing Poetry before PyEnv, as 
they both alter PATH in a way that can cause issues if installed in the 
wrong order. 

### Installing dependencies
Open a shell in the project folder and run `poetry install`

### Running the application
In shell, run `poetry shell` to start the virtual environment. Once you've 
done this, you're free to run any of the python commands below. Remember to 
run it if you open a fresh terminal window. 

To quickly create a SQLite database, run
```shell
python manage.py runserver
```
Let it start, then kill it using Ctrl-C.

Next we'll migrate the database and load the data in. I've written a simple 
Django command to do the data loading. Insert the test data JSON file into 
the top-level project folder, then run the following:
```shell
python manage.py migrate
python manage.py load_startlist <filename.json>
```

Once that's done, you can start the server as follows:
```shell
python manage.py runserver
```

And access the server at [127.0.0.1:8000](http://127.0.0.1:8000)

The main endpoint for creating and updating tickets can be found at 
[/races/tickets/](http://127.0.0.1:8000/races/tickets/)

## Application Design

### Overview
The REST API is written in Django, using Django REST Framework. I chose this 
because it provides a lot of powerful features for building filterable, 
paginated backends with minimal code.

### Data modelling & database
While the focus of the exercise wasn't on data modelling or creating a 
database, I've chosen to use one as it's difficult to leverage the features 
of Django and Django REST Framework (DRF) without one. 

For the sake of time, I've modelled a subset of the total fields of the 
source data, skipping some of the fields like gender, address and phone 
number. Hopefully it's easy to see how the solution would extend to adding 
these.

I've also loaded the data in more or less as-is, as I read the spirit of the 
exercise to implementing the API more than correctly modelling and massaging 
the data. As a result, it's unnormalised despite hints that event, race, 
ticket, etc. could be modelled as their own entities.

Note: I've called each entry a 'Ticket' meaning a single persons record of 
entry into the race. I realised late that this is somewhat ambiguous with 
the modelling of ticket in the source data meaning a *type* of ticket. 
Given more time I'd have found a better name for this, but I've stuck to 
'Ticket' in the discussions that follow.


## Features implemented
The API can do the following, all accessed at [/races/tickets/](127.0.0.1:8000/races/tickets/):
- List all tickets via a cursor paginated view, suitable for infinite scrolling
- Provides filtering on `eventId`, `raceId`, `ticketId` on the above list view, 
  with scope to add more filters as needed
- Create a new ticket by POSTING to the endpoint. A new ticket has it's 
  `created_at` and `updated_at` values set by the server

I unfortunately didn't get to implement search, but it would be easy to add 
in the future. See 'Implementation - Filtering' below

## Playing with the API
Django REST framework provides an HTML interface for testing the API, which 
you can access at the provided URL. In case you've never used it before, I'd 
point out:
- There is a form to POST data at the bottom, below the returned results
- You can test the filters by adding query params to the URL manually, but
there is also a form which can be opened by clicking 'Filters' near the top 
  right
- Next and previous buttons are provided to paginate

## Implementation - Filtering
Filters have been implemented on the view using [`django-filter`](https://www.django-rest-framework.org/api-guide/filtering/)
and it's integration with Django REST Framework. See the docs for the full 
list of options, which can be configured by editing the config in the 
`ListCreateTickets` view.

Currently only exact match filtering is implemented. Adding more complex 
filters is a case of defining custom FilterSets as per the docs, which would 
also allow you to implement search by whatever search scheme/criteria you 
desire.

## Implementation - Pagination
Implemented using [CursorPagination](https://www.django-rest-framework.org/api-guide/pagination/), using `created_at` as the ordering field, newest 
entries first. You can change the ordering criteria by editing `races.views.
TicketsPagination`.

## Tests
I've written fairly minimal automated tests, partly for time but also 
because they would largely be testing framework code. I have written one 
test covering creating a new ticket via the API. You can run the test suite 
using:

```shell
python manage.py test
```

