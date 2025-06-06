# Certura Task 2

## How to Run the Project

1. **Install dependencies:**
   
   ```powershell
   pip install -r requirements.txt
   ```

2. **Initialize the database and create a test user:**
   
   ```powershell
   python init_db.py
   ```

3. **Run the Flask app:**
   
   ```powershell
   python run.py
   ```

---

## How to Test the API

You can test the API using tools like [Postman](https://www.postman.com/) or `curl`. Here is an example using Python's `requests` library:

```python
import requests

url = "http://localhost:5000/login"  # Change endpoint as needed
data = {
    "username": "testuser",
    "password": "testpass"
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

- Replace the URL and endpoint as per your API routes.
- Make sure the Flask app is running before testing the API.

---

**Contact:** For any issues, please contact the project maintainer.
