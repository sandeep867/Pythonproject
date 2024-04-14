from django.shortcuts import render
import os
from robot.api import TestSuiteBuilder
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from robotframeworkproject.settings import BASE_DIR


# Create your views here.

def TestAutomation(request):
    if request.method == 'POST':
        # Construct the path to the test case file
        test_case_path = os.path.join(BASE_DIR, 'robotframework_tests', 'Test_case_1.robot')

        # Check if the test case file exists
        if os.path.exists(test_case_path):
            # Build the Robot Framework test suite
            suite = TestSuiteBuilder().build(test_case_path)

            # Execute the tests
            results = suite.run(output=None)

            # Check test results and return response
            if results.return_code == 0:
                return JsonResponse({'status': 'Passes', 'details': results.suite.status})
            else:
                return JsonResponse({'status': 'Failed', 'details': results.suite.status})
        else:
            return JsonResponse({'error': 'Test case file not found'})
    else:
        # If the request method is not POST, render the HTML form
        return render(request, 'tests/Automation.html')
