# Transpose a matrix

### Prerequisites

- `pip3 install -r requirements.txt`

## Usage
Start the server
```
python3 server.py
```
Hit the URL `127.0.0.1:5000/transpose` with a POST request

Request format:
```
{
  "matrix": [[1,2],[3,4]]
}
```
Response format:
```
{"error":"","result":[[1,3],[2,4]]}
```
