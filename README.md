
![Architecture](https://github.com/sousou15/Backdoor/assets/43934641/84b6a1f2-7e5c-4399-944d-2f67b604a063)


# RAT in python

This is a functional version but it is also a very simple one and has a couple of bugs.

I made this project just for fun and I am currently working on it to improve it and incorporate an interface.
The reverse connection module is still not working properly.

To expose it to the internet, forward with TCP. Example: ngrok tcp 8080. We are working with sockets.


Additionally, you can find some commands that can be executed if you dig into NOTES.txt. We can schedule the executable as a task to run at intervals to re-establish the connection.
We can use curl along with the Hermes, Loki, and Hestia servers. Those are mythological names related to what the module does.


# Modules 

For now, ports and hosts can be customized on the code.

-Maat: Grants comprehensive access to target systems, facilitating command execution, file manipulation, and reconnaissance. Based on sockets. TCP. 

-MaatReverse: Establishes a covert bind connection, enabling communication from the target to the operator's server. The target acts like server and waits for connections. Bind shell. Just some weird stuff I am trying.

-Hestia: Endpoint for file retrieval from the target system. It has 2 modules, one with public ip checker and the other only resolves local hosts. Server. Port: 5000

-Loki: Allows file downloads from target system. Server. Port: 8000

-Hermes: Injects files into target system, seamlessly integrating them into directories for future use. Server. Port: 3030

-Argos: Captures target screen activity, providing a visual file. Server. Port: 3030
 

