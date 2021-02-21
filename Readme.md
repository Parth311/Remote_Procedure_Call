# Lab Activity-2
- Uploaded `4` files in the zip folder `2020201054_lab2.zip`
- `server.py`: python file holding the function definitions. 
- `client.py`: python file calling the functions which are defined in `server.py`.
- `rpc.py`: python file that dynamically generates the `client_stub.py` file. 
- `client_stub.py`, `server_stub.py`: intermediate files to carry out RPC communication. 
## Flow of Execution
- user adds the function definitions at the server side, i.e `server.py`
- `rpc.py` is executed which generates the `client_stub.py` file with all the func definitions in the `server.py` file.
- `server_stub.py` is executed which listens on `port 7004` and waits for a client to join.
- `client.py` is executed through which user calls the desired function through `client_stub.py` by establishing a connection with the server stub.  
