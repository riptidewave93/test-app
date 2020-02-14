# test-app

A basic flask web API app.

## Installing Requirements
```
sudo pip3 install -r ./requires.txt
```

## Running Tests

We use pytests to verify that our app works as expected
```
py.test
```

Manually verifying:
  1. Run the app (see Running Section)
  2. Verify responses
  ```
  curl http://127.0.0.1:5000/
  curl -H "Accept: application/json" http://127.0.0.1:5000/
  curl -X POST http://127.0.0.1:5000/
  ```

## Running

In Debug Mode:
```
DEBUG=True flask run
```

In Standard Mode:
```
flask run
```
