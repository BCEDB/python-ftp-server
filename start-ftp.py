import shutil
import os

try:
    # Try to import the pyftpdlib library.
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer

except ImportError:
    # If the pyftplib library cannot be imported. Try to install it for the user.
    os.system('python -m pip install pyftpdlib')

    # Then try to import the pyftpdlib library (again).
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer

host = '127.0.0.1'
port = 21
username = 'username'
password = 'password'
path = 'C:/FTPServer/'

# Check if the FTP server folder already exists.
if( os.path.exists( path ) == False ):
    # The folder does not already exist, create the folder and
    # copy the Contents of the FileSystem folder onto the FTP Server.
    shutil.copytree( 'FileSystem', path )

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