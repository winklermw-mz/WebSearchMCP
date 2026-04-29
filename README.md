# MCP Server

This is a simple server application built using FastMCP, designed to execute web searches and Wikipedia queries.

## Provided Tools

- `search_web`: Performs internet searches to query unknown or recent data using DuckDuckGo.
- `search_wikipedia`: Queries Wikipedia for more detailed information on specific topics.
- `get_current_date`: Returns the current date in a formatted string.
- `get_current_location`: Returns the fixed location of the user (currently set to Mainz, Germany, can be specified in `utils/config.py`).

## Requirements

- Python 3.x
- Other dependencies as specified in `requirements.txt`

## Installation

1. Clone or download this repository.
2. Ensure all required dependencies are installed.

```bash
pip install fastmcp requests ddgs beautifulsoup4 wikipedia colorama
```

3. Run the server:

```bash
python mcp_server.py
```

## Usage

The MCP Server runs on `http://0.0.0.0:8010/mcp`. You can interact with the server using the provided tools.

## Docker

The server can be run in a docker container. A docker file as well as a setup script `create_docker_image.sh` is available.