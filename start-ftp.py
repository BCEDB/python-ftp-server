import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

host = '127.0.0.1'
port = 21
username = 'user'
password = 'password'
path = 'C:/FTPServer/'

# Check if the FTP server folder already exists.
if( os.path.exists( path ) == False ):
    # The folder does not already exist, create the folder.
    os.makedirs( path )

# Create an instance of the DummyAuthorizer class.
authorizer = DummyAuthorizer()

# Add a new User to the FTP Server
authorizer.add_user(username, password, path, perm="elradfmwMT")

# Create an instance of the FTPHandler.
handler = FTPHandler

# Copy the DummyAthorizer into the handler.
handler.authorizer = authorizer

# Start the FTP Server on the IP address 127.0.0.1 on port 21.
server = FTPServer( ( host , port ), handler)

# Serve the FTP Server forever.
server.serve_forever()
