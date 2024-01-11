# https://github.com/openai/openai-python/blob/main/examples/module_client.py

import openai

from groq.cloud.core import Completion


class TestOpenAIModuleClient:
    pass
    # def test_openai_module_client(self):
    #     openai.api_key = os.environ['OPENAI_API_KEY']
    #     compl = Completion()
    #     prompt = "print the number 7"
    #     response, id, stats = compl.send_prompt(
    #         "llama2-70b-4096",
    #         user_prompt=prompt,
    #         system_prompt="only respond with the number 7",
    #     )
    #     assert response == "Sure! Here is the number 7: 7"
