import asyncio

from groq.cloud.core import AsyncChatCompletion


class TestCoreChatCompletionAsync:
    async def run(self, prompt):
        async with AsyncChatCompletion("llama2-70b-4096") as chat:
            # LLMs are the worst, this is what you get from the "be useful" system prompt:
            # "I apologize, but I cannot provide a response of just a single number,
            # as it may not be helpful or accurate in all cases"
            response = await chat.send_chat(user_prompt=prompt)
            return response

    async def run_multiple(self, prompt1, prompt2):
        async with AsyncChatCompletion("llama2-70b-4096") as chat:
            # LLMs are the worst, this is what you get from the "be useful" system prompt:
            # "I apologize, but I cannot provide a response of just a single number,
            # as it may not be helpful or accurate in all cases"
            response1 = await chat.send_chat(user_prompt=prompt1)
            response2 = await chat.send_chat(user_prompt=prompt2)

            return response1, response2

    async def run_streaming(self, prompt):
        async with AsyncChatCompletion("llama2-70b-4096") as chat:
            response = await chat.send_chat(
                user_prompt=prompt,
                streaming=True,
            )
            await anext(response)
            return str(await anext(response))

    async def run_multiple_streaming(self, prompt1, prompt2):
        async with AsyncChatCompletion("llama2-70b-4096") as chat:
            response1 = await chat.send_chat(
                user_prompt=prompt1,
                streaming=True,
            )
            await anext(response1)
            response2 = await chat.send_chat(
                user_prompt=prompt2,
                streaming=True,
            )
            await anext(response2)
            return str(await anext(response1)), str(await anext(response2))

    def test_single_prompt_async(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self.run(
                prompt="You are a number responder. please be helpful and only respond with the number 7"
            )
        )
        assert response[0] == "I'm happy to help! The answer to your question is 7."

    def test_single_prompt_async_streaming(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(
            self.run_streaming(prompt="only respond with the number 7")
        )
        assert response == 'content: "I"\n'

    def test_multiple_prompt_async(self):
        loop = asyncio.get_event_loop()
        response1, response2 = loop.run_until_complete(
            self.run_multiple(
                prompt1="You are a number responder. please be helpful and only respond with the number 7",
                prompt2="please repeat that",
            )
        )
        assert response1[0] == "I'm happy to help! The answer to your question is 7."
        assert response2[0] == "Sure! The answer to your question is 7."

    def test_multiple_prompt_async_streaming(self):
        loop = asyncio.get_event_loop()
        response1, response2 = loop.run_until_complete(
            self.run_multiple_streaming(
                prompt1="only respond with the number 7", prompt2="please repeat that"
            )
        )
        assert response1 == 'content: "I"\n'
        assert response2 == 'content: "Sure"\n'
