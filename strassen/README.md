# Strassen Package Detail
It Is Strassen Algorithm And Distribute Strassen Multiplication To 7 Strassen Multiplication And Send Them To Other Clients For Calculation.


# 1. Strassen.py

### Constructor
Get 3 Parameter. Two Matrices And List Of Other Server Ports.

```python
class Strassen:
    __init__(self, matrix_01, matrix_02, port_list=None)
```

### Methods
-   **calculate(self)**: If Port List Is Not Empty, Strasssen Calculate Muliplication By Propagate Matrices To Other Clients (propagate_calculate). But If Port List Is Empty, Strassen Calculates Muliplication Locally (self_calculate).

-   **propagate_calculate(self)**: Creates CalculateThread For Each M1 - M7 Matrices With Random Port For Connection. Run Them Until True Result Obtained. If A Thread Cause Problem Or Result Be None, Create New Thread With New Random Port And Run It Again.

-   **self_calculate(self)**: Calculate Multiplications (M1 - M7) By Create Local Strassen Object Recursivly.


# 2. calculatethread.py

### Constructor
Get 3 Parameter. Server Port To Connection And Two Matrices For Sending To Server.

```python
class CalculateThread(Thread):
    __init__(self, port, matrix_01, matrix_02)
```

### Methods
-   **run(self)**: Override Thread Run Method. When Thread Start, It Tries Connect To Given Port. After Connection, Sends Two Matrices To Server And Wait For Get Result Matrix. Then Closes The Connection.

-   **get_matrices(self)**: Return Tuple For Two Matrices Of This Thread When Thread Faild Or Result Is None.

-   **get_result_matrix(self)**: Return Result Matrix Of This Thread.
