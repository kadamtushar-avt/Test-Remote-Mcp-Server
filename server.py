from fastmcp import FastMCP
import random
import json


mcp = FastMCP("Simple Calculator server")

@mcp.tool()
def add(a:int,b:int)->int:

    """ Add two numbers together
        Args:
        a:first number
        b:second number

        Returns:
        the sum of a and b
    """

    return a + b

@mcp.tool()
def random_number(min_val:int=1,max_value:int=100)->int:
    """ Generate a random number within a range

        Args:
        min_value:Minimum value(default 1)
        max_value:Maximum value(default 100)

        Returns:
         A random integer between min_value and max_value
    """

    return random.randint(min_val,max_value)

@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server"""
    info = {
        "name":"Simple Calculator server",
        "version":"1.0.0",
        "description":"A basic mcp server with math tools",
        "tools":["add","random_number"],
        "author":"Tushar"
    }


    return json.dumps(info,indent=2)


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)