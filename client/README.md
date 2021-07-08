# Client Package Detail


# 1. Methods.py
Some Methods That Used For Client CLI Or Client Calculations.

-   **add_matrix(matrix_01, matrix_02)**: Add Two NxN Matrices

-   **subtract_matrix(matrix_01, matrix_02)**: Subtract Two NxN Matrices

-   **multiply_matrix(matrix_01, matrix_02)**: Multiplication Of Two NxN Matrices With Normal Algorithm

-   **split_matrix(matrix_obj)**: Split One Matrix To 4 Matrices. For Example Matrix A To 4 Part Of A11, A12, A21, A22

-   **concat_matrices(matrix_11, matrix_12, matrix_21, matrix_22)**: Turn 4 Matrices To One Complete Matrix

-   **get_matrix_from_user(name)**: Get Matrix From User Input In CLI Row By Row And Seprated By Comma(,)

-   **read_matrix_from_file()**: Get Number Of File Name From User CLI And Read Two Matrices From './files/number.txt' File


# 2. Matrix.py
Class For Keep 2 Dimension Array Like One Matrix Object.

### Constructor
One 2 Dimension Array For Creating Matrix Object.

```python
class Matrix:
    __init__(self, matrix=None)
```

### Methods
-   **set_matrix(self, matrix)**: Set 2 Dimension Array For Matrix Object

-   **get_matrix(self)**: Get 2 Dimension Array Of Matrix Object

-   **get_dimension(self)**: Return Int Number Of Matrix Array Rows

-   **__str__(self)**: Uses Array To String Method For Print Or Show Matrix Object


# 3. Client.py
Main Client For Connectiong To This Network.

### Constructor
With Create A Client, It Creates A Socket For Connection And Server Beside Itself.

```python
class Client:
    __init__(self)
```

### Methods
-   **connect(self, host, port)**: Connects Socket To Given Host And Port And Then Starts Server Thread

-   **close(self)**: Close Client Socket Connection To Network

-   **get_client_server_ports(self)**: sends A Message Of Type REQ_LIST To Main Server For Get List Of Other Clients Server Port. Then Should Receive Message With Type LIST From Main Server That Contain List Of Ports

-   **calculate_strassen(self, matrix_01, matrix_02)**: Create Strassen Object With List Of Port That Gets From Main Server And Two Matrices Of Method Argument. After Calculation, Returns Result


# 4. Sthread.py
Server Thread That Runs Beside Main Client. It Runs On A Random Port And Sends It's Port To Main Server By Client.

### Constructor
Main Client Object To Interact With Main Server Socket For Send Or Receive Message.

```python
class ServerThread(Thread):
    __init__(self, main_client)
```

### Methods
-   **run(self)**: Override Thread Run Method. Try To Run Server On Random Port Between 40000 To 60000. When Connection Was Succesful, Send Random Port To Main Server With Message Type Of MY_PORT

-   **listen(self)**: Listen For Connection From Other Clients. When A Connection Accepted, Creates ServerClientThread For Get Matrices And Calculate Strassen


# 5. Scthread.py
Listen On Server Accepted Socket For Get Matrices And Calculate Strassen And Send Back Result To Socket.

### Constructor
Main Client For Use Calculate Methods Of Client And Connection Socket For Send And Receive Messages.


```python
class ServerClientThread(Thread):
    __init__(self, main_client, client_socket, address)
```

### Methods
-   **run(self)**: Override Thread Run Method. When A Matrix Received From Connection Socket, Adds It To A List. When List Length Was Enough For Multiplication, Use Main Client calculate_strassen Methods For Calculate Result. At The End Send Back Result To Socket And Clears List Of Matrices.
