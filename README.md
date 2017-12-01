# flounder
flounder is a library that create Entity of Dialogflow.
This library uses RestAPI of dialogflow. It is not an official library.

## Installation

### flounder requires:

```
pip install git+https://github.com/miurahr/pykakasi.git
```

### install flounder:

```
pip install flounder
```

## Example

```py:test_entity_upload.py
from flounder.flounder import Flounder

flounder = Flounder(DEVELOPER_ACCESS_TOKEN)
create_request = flounder.create_request('Sushi', 'sushi.csv')
response = create_request.getresponse()

print (response.read())
print (response.status, response.reason)
```

### CSV

```text:sushi.csv
"鯖"
"鯵"
"鰈"
"鱸"
"鮑"
"鮪"
"鯨"
"鮭"
```

```
$ python test_entity_upload.py
```

## License
flounder is licensed under MIT License. See LICENSE for more information.