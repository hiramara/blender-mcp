from blender_mcp.server import main as server_main
import sys

def main():
    """Entry point for the blender-mcp package.
    
    Runs the MCP server that connects Blender to Claude via the
    Model Context Protocol. Requires Blender to be running with
    the blender-mcp addon enabled.
    """
    server_main()

if __name__ == "__main__":
    main()
