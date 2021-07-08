# Server Package Detail
It Is About Creating Main Server And Resolve Client Request To Main Server.

# 1. Server.py

### Constructor
Create Main Server Socket And Dictionary For Keep List Of Client's Server Ports.

```python
class Server:
    __init__(self)
```

### Methods
-   **bind(self, host, port)**: Bind Server Sokcet To Given Host And Port

-   **listen(self)**: Server Socket Listen For Accept Clients. When Client Connected, Creates ClientThread For Each Client To Send Or Receive Message To That Client.

-  **add_server_port(self, client_port, server_port)**: Add server_port To Dictionary With Key Of client_port

-   **remove_server_port(self, client_port)**: Removes Server Port From Dictionary With Key Of client_port

-   **get_client_server_ports(self, client_port_filter=None)**: Filter Dictionary Values That Their Key Is Not client_port_filter And Return List Of Ports.


# 2. Cthread.py

### Constructor
Server And Client Instract With This Thread. It Listen To Clinet Socket For Receive Request And Get Information From Server Object And Send It Back To Client Socket.
3 Argument Of This Class Is: Main Server Object, Connected Client Socket, Tuple Of Client Address And Port

```python
class ClientThread(Thread):
    __init__(self, server, client_socket, address)
```

### Methods
-   **run()**: Override Thread Run Method. Listen For Receive Message From Client Socket. Main Server Can Resolve 2 Type Of Messages. Type Of MY_PORT For Getting Client's Server Port And Add It To Server Dictionary And Type Of REQ_LIST That Server Should Filter Dictionary By Client Port And Send It Back List Of Other Clients Port. Also When A Client Disconnect From Network, Server Should Remove It's Information From Server Dictionary.
