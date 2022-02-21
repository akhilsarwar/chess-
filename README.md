# MULTIPLAYER CHESS GAME

## About
A multiplayer chess game 


![](/readme-assets/chess.gif)

## Installation
```python
pip3 install -r requirements.txt
``` 

## Setup

### Server
Server code be run on any cloud servers. Deployment in aws can be found 
[here](#setting-up-server-code-in-aws)

- Navigate to the server directory
```
cd server
```

- Run the server.py file
```python
python3 server.py
```

### Client
- Run 
```python
python3 client.py
```


## Instructions:
- You will be prompted to enter the username before starting the game.

- Board contains white and black pieces oriented in a way that the current player's pieces move in upward direction.

- After every move previos move will be highlighted in green.

- A check is followed by a red highlight.
- A checkmate is followed by a purple highlight.

 - Currently it supports only a game at a time and the first user has to wait until the second user arrives.


## Setting up server code in aws

 - Connect to your instance using SSH. Use the SSH key pair that was assigned to your instance when you launched it and use the default user name of the AMI that you used to launch your instance. 
 ```bash
 ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-public-dns-name
 ```

 - Transfer the server code
 ```bash
 scp -i /path/my-key-pair.pem /path/server/server.py ec2-user@my-instance-public-dns-name:path/
 ```
 - More info can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
