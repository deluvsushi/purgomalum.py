# purgomalum.py
Web-API for [purgomalum.com](https://www.purgomalum.com) web service for filtering and removing content of profanity, obscenity and other unwanted text

## Example
```python
import purgomalum
purgomalum = purgomalum.Purgomalum()
response = purgomalum.call_web_service(text="", add="", fill_text="", fill_char="")
print(response)
```
