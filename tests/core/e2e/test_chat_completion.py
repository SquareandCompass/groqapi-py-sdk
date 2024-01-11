from groq.cloud.core import ChatCompletion


class TestCoreChatCompletion:
    def test_single_prompt(self):
        with ChatCompletion("llama2-70b-4096") as chat:
            prompt = "print the number 7"
            response, id, stats = chat.send_chat(prompt)
            assert response == "Sure! The number 7 is: 7"

    def test_single_prompt_streaming(self):
        with ChatCompletion("llama2-70b-4096") as chat:
            prompt = "print the number 7"
            response = chat.send_chat(prompt, streaming=True)
            # needed to skip nondet request id
            next(response)
            assert str(next(response)) == 'content: "Sure"\n'

    def test_multiple_prompt(self):
        with ChatCompletion("llama2-70b-4096") as chat:
            prompt = "print the number 7"
            response, id, stats = chat.send_chat(prompt)
            assert response == "Sure! The number 7 is: 7"
            prompt = "can you repeat that?"
            response, id, stats = chat.send_chat(prompt)
            assert response == "Sure! The number 7 is: 7"

    def test_multiple_prompt_streaming(self):
        with ChatCompletion("llama2-70b-4096") as chat:
            prompt = "print the number 7"
            response = chat.send_chat(prompt, streaming=True)
            # needed to skip nondet request id
            next(response)
            assert str(next(response)) == 'content: "Sure"\n'
            prompt = "can you repeat that?"
            response = chat.send_chat(prompt, streaming=True)
            # needed to skip nondet request id
            next(response)
            assert str(next(response)) == 'content: "Sure"\n'
