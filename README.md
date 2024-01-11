# GroqAPI for Python
[![PyPI version](https://badge.fury.io/py/groq.svg)](https://badge.fury.io/py/groq)

## Installation 

To install the GroqAPI Python Library, you can just use `pip`:
```bash
pip install groq
```

## Usage

Make sure to export your access key to the `GROQ_SECRET_ACCESS_KEY` environment variable.

```python
from groq.cloud.core import ChatCompletion

with ChatCompletion("llama2-70b-4096") as chat:

    prompt = "Is AI fun or what?"

    response, _, _ = chat.send_chat(prompt)

    print(response)
```
Look at our `/examples` folder for more examples.
