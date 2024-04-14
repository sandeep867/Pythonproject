*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google Homepage
    sleep    3
    Open Browser    https://www.google.com    chrome
    maximize browser window
