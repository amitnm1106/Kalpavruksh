# Test pattern for Python is as follows:

The Columns for Question, Answer, User and Tenant Table is as follows: 
1. Question table consist of columns Title, private, user_id
2. Answer table consist of columns body, question_id, user_id
3. Tenant table consist of name and api_key
4. User table consist of name

Populate the fake data in all tables using by running following script.
```
run scrap_question_answer.py
```

# Accomplish the following tasks using Django or any other framework in python:
1. Add a RESTful, read-only API to allow consumers to retrieve Questions with Answers as JSON (no need to retrieve Answers on their own). The response should include Answers inside their Question as well as include the id and name of the Question and Answer users.
2. Don't return private Questions in the API response.
3. Require every API request to include a valid Tenant API key, and return an HTTP code of your choice if the request does not include a valid key.
4. Track API request counts per Tenant.
5. Add an HTML dashboard page as the root URL that shows the total number of Users, Questions, and Answers in the system, as well as Tenant API request counts for all Tenants. Style it enough to not assault a viewer's sensibilities.
6. Add tests around the code you write as you deem appropriate. Assume that the API cannot be changed once it's released and test accordingly.
7. You are welcome to add any models or other code you think you need, as well as any gems.
8. Allow adding a query parameter to the API request to select only Questions that contain the query term(s). Return an appropriate HTML status code if no results are found.
9. Add a piece of middleware to throttle API requests on a per-Tenant basis. After the first 100 requests per day, throttle to 1 request per 10 seconds.
