# Minecraft Library for Empower Servers
I have a bedrock server from Empower Servers which has a nice web based console and I thought I'd make a little class to send commands to it from my python scripts.

## Installation
You will need selenium, the quickest way to install this is this: 
```pip install selenium```

Currently this project is only working on Macs with Safari however cross browser support is possible.

## Basic use
```from minecraft import empower_server

 server = "server uuid"
 user = "user@email.com"
 password = "xxxxxxxx"

 command = "setblock 0 0 100 sandstone"
  mc = minecraft.empower_server(server, user, password)
 mc.sendCommand(command)
 mc.setBlock(0,0,100,"air")
 mc.close()
 ```

