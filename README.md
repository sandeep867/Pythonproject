<html>
<body>
<h3>API Test Automation System with Robot Framework:</h3>
<p>
    The primary goal of this project is to develop a system capable of accepting detailed API calls, executing specified testing steps as Robot Framework tests, and returning the test output. This involves creating an application using Python and Django that exposes an API endpoint. The endpoint is designed to accept POST requests with a specific structure, carry out the provided steps using Robot Framework, and finally, deliver the test results.
</p>

<h3>Prerequisites:</h3>
<ul>
    <li>Python installed on your system (recommended version 3.x)</li>
    <li>Django framework installed (pip install django)</li>
    <li>Robot Framework installed (pip install robotframework)</li>
</ul>

<h3>Steps:</h3>
<ol>
    <li>Create a Django project:</li>
    <ul>
        <li>django-admin startproject robotframeworkproject</li>
    </ul>
    <li>Create a Django app within the project:</li>
    <ul>
        <li>cd robotframeworkproject</li>
        <li>python manage.py startapp robotframeworkapp</li>
    </ul>
    <li>Define the URL patterns:</li>
    <ul>
        <li>Open robotframeworkapp/urls.py and define the URL patterns for your app. Add the endpoint for executing tests as per the provided challenge specification.</li>
    </ul>
    <li>Implement views:</li>
    <ul>
        <li>Open robotframeworkapp/views.py and implement the view function TestAutomation to handle the POST requests and execute the tests using Robot Framework. Use the provided code snippet as a reference.</li>
    </ul>
    <li>Configure the Django project settings:</li>
    <ul>
        <li>Configure the installed apps, middleware, database settings, etc., in robotframeworkproject/settings.py as needed.</li>
    </ul>
    <li>Create Robot Framework test suite:</li>
    <ul>
        <li>Write the robotframework_tests/Test_case_1.robot to cover the functionalities specified in the challenge. These test cases should be written in .robot files and saved in a directory within your project.</li>
    </ul>
    <li>Install required Python packages:</li>
    <ul>
        <li>Install any additional Python packages required for your project, such as robotframework, robotframework-seleniumlibrary, etc., using pip install.</li>
    </ul>
    <li>Run the Django development server:</li>
    <ul>
        <li>python manage.py runserver</li>
    </ul>
    <li>Test the API:</li>
    <ul>
        <li>Use tools like Postman or any other API testing tool to send a POST request to the API endpoint (http://127.0.0.1:8000/testai/tests/v1/execute) with the specified JSON payload.</li>
    </ul> 
    <li>Verify functionality:</li>
    <ul>
        <li>Verify that the tests are executed successfully.</li>
    </ul>
</ol>

<h3>API Call Examples :</h3>
<p>
    {
  "tests": [
    {
      "title": "Open Google",
      "steps": [
        "Open Browser    browser=chrome",
        "Go To    url=https://www.google.com"
      ]
    }
  ]
}<br />
<p> After executing this we would get a validation if the automation was pass or fail</p>

</p>

</body>
</html>
