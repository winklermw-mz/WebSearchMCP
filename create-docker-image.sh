docker build -t winklermw-mz/websearchmcp .
docker run -d --name WebSearchMCP --network my-local-net -p 8010:8010 winklermw-mz/websearchmcp