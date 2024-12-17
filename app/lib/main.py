from flask import app
from lib.cli import cli  

if __name__ == '__main__':  
    cli()

from config import Config  

app.config.from_object(Config)