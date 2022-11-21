*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***

Register With Valid Username And Password
    Input Credentials  uusin  uusi1235
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  elsa  validpassword123
    Output Should Contain  User with username elsa already exists

Register With Too Short Username And Valid Password
    Input Credentials  el  validpassword1234
    Output Should Contain  Invalid username (minimum 3 characters)

Register With Valid Username And Too Short Password
    Input Credentials  asle  short1
    Output Should Contain  Invalid password (minimum 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  valid  validpasswordcontainingonlyletters
    Output Should Contain  Invalid password (contains only characters)


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  elsa  elsaaaaa123
    






