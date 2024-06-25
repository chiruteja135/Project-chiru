*** Settings ***
Library    DatabaseLibrary

*** Variables ***
${DBNAME}    test.db
${DBFILE}    ${CURDIR}${/}${DBNAME}

*** Keywords ***
Connect To SQLite Database
    Connect To Database    sqlite3    ${DBFILE}    ${EMPTY}    ${EMPTY}    ${EMPTY}

Insert Data Into SQLite Database
    ${query}=    Set Variable    INSERT INTO users (name, email) VALUES ('Raj Sharma', 'raj.sharma@example.com')
    Execute Sql String    ${query}

Verify User Exists In SQLite Database
    ${query}=    Set Variable    SELECT * FROM users WHERE email = 'raj.sharma@example.com'
    ${rowcount}=    Row Count    ${query}
    Should Be True    ${rowcount} > 0    User not found in the database.

*** Test Cases ***
SQLite Database Test
    Connect To SQLite Database
    Insert Data Into SQLite Database
    Verify User Exists In SQLite Database
    Disconnect From Database
