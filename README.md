# Distributed Network To Calculate Matrices Multiplication With Strassen Algorithm


## How It Works
It Is A Network That Can Calculate Matrix Multiplication With Strassen Algorithm.
First, You Should Run Main Server. All Clients That Wants To Connect Network Should Introduce Itself To Main Server.

When A Client Run, It Runs A Server Beside Itself As A Thread. Server Run On Random Port Between 40000 - 60000.
When The Server Is Set Up, Send It's Running Port For Main Server By Client. Main Server Keep List Of All Server Ports
For Each Client That Connected To Network. Client's Server Is Listening For Multiplication Request From Other Clients.
When Client's Server Receive Multiplication Request, If Matrix Is 2X2 Calculates It But If Not Split It To 4 Matrices And Send Them To Other Clients Server For Calculation.

You Can See Detail Of Strassen Algorithm On
[Wikipedia Strassen Algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm).
After That Can You Can Continue Reading.


## Clients In Detail
When A Client Connect To Network It Runs Server For Get Calculation Request. Each Client Can Send Matrices On Network
For Calculation. If There Is No Other Clients On Network, Client Calculate Multiplication Itself By Strassen Algorithm
Recursively.

If Network Is Not Empty, Client Send Request To Main Server For Get List Of Other Client's Server Port. Strassen
Has 7 Recursive Strassen Multiplication And 18 Add - Subtraction Matrix. Client Choose 7 Random Port From List And
Send Each Multiplication To Other Clients With A Thread. When Each Thread Ends, If There Is Problem In Calculation Or
Connection To Other Client's Server, Result Should Be None And Client Should Create New Thread With New Random Port.
Client Wait For Each 7 Threads To Be Finished And M1 - M7 Be Calculated.

Now C11, C12, C21, C22 Can Be Calculated From M1-M7 By Add - Subtraction Matrix. Client Concat Them To Create Main
Result Matrix.

This Process Run Recursively To All 7 Client And Result Back. At The End Main Client Print Result.


## Message Protocol
Each Message That Sends On This Network Has 2 Part As A Dictionary.

```python
    message = {
        'type': msg_type,
        'message': message
    }

    size = len(message)
```
This Dictionary Serilize As Json String. First Message Sends Size Of This String In 10 Constant Byte As A Number.

In Receiver Side, First Get 10 Byte Constant Size Of Message And Then Get Size Byte Message From Sokcet. Then Deserialize This String As Dictionary And Return It To Upper Layer.


## Message Types
Name | Value | Deatil
-----|-------|--------
MY_PORT| 0 | Client's Server Send Port To Main Server
MATRIX| 1 | Send Matrix On Network
REQ_LIST| 2 | Request Lits Of Server Ports From Main Server
LIST| 3 | Send Array Of Ports List From Main Server To Client


--------------------------------------------------


# Root Files Detail


### 1. Main.py
Get Input From User To Run Main Server Or Client.

If Run Server, CLI Wait For Print Connection Logs.

If Run Clinet, CLI Can Get Input From User Again.
There Is 2 Way For Send Matrix On Network. By Enter Matrix By CLI And Each Row Elements Seprated By Comma(,) Or Read Two Matrix From File As Json Array.


### 2. Generic.py
There Is 2 Global Constant For General Use Purpose.

-   **HOST, PORT**: Main Server Host And Port For Connection

-   **MSG_TYPE**: Type Of Sended Messages In This Network


### 3. Methods.py
Some Methods That Are Global In Server Or Client User.

-   **send_message(socket, msg_type, message)**: Send Message To A Socket By Message Send Protocol
-   **receive_message(socket)**: Receive Message From A Socket By Receive Protocol

-   **print_line()**: Print Line Of Dash(-) In CLI

-   **get_int(message)**: Show Message In CLI And Get Int Input From User By Catch Of Invalid Input
