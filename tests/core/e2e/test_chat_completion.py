from groq.cloud.core import ChatCompletion


class TestCoreChatCompletion:
    def test_chat_completion(self):
        with ChatCompletion("llama2-70b-4096") as chat:
            prompt = "print the number 7"
            response, id, stats = chat.send_chat(prompt)
            assert response == "Sure! The number 7 is: 7"

    def test_chat_completion_streaming(self):
        with ChatCompletion("llama2-70b-4096") as chat:
            prompt = "print the number 7"
            response = chat.send_chat(prompt, streaming=True)
            # needed to skip nondet request id
            next(response)
            assert str(next(response)) == 'content: "Sure"\n'
