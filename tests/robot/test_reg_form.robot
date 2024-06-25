*** Settings ***
Library    SeleniumLibrary
Library    csv_reader.py

*** Variables ***
${URL}    http://localhost:5000
${CSV_FILE_PATH}    C:/Users/ycycr/project-chiru/tests/robot/students.csv

*** Test Cases ***
Submit Form With Valid Data

    Open Browser    ${URL}    chrome

    @{csv_data}    read csv data    ${CSV_FILE_PATH}
    FOR    ${row}    IN    @{csv_data}
        ${name}    ${email}    ${phone}    ${dob}    ${hometown}    Evaluate    $row
        Submit Form With Data    ${name}    ${email}    ${phone}    ${dob}    ${hometown}
    END

    Close Browser

*** Keywords ***
Submit Form With Data
    [Arguments]    ${name}    ${email}    ${phone}    ${dob}    ${hometown}
    Log    Name: ${name}, Email: ${email}, Phone: ${phone}, DOB: ${dob}, Hometown: ${hometown}
    Wait Until Element Is Visible    id=name
    Input Text    id=name    ${name}
    Input Text    id=email    ${email}
    Input Text    id=phone    ${phone}
    Input Text    id=dob    ${dob}
    Input Text    id=hometown    ${hometown}
    Click Button    css=input[type="submit"]
    Wait Until Page Contains    Data submitted successfully
    Capture Page Screenshot