import asyncio

from groq.cloud.core import AsyncChatCompletion


class TestCoreChatCompletionAsync:
    async def run(self):
        async with AsyncChatCompletion("llama2-70b-4096") as chat:
            # LLMs are the worst, this is what you get from the "be useful" system prompt:
            # "I apologize, but I cannot provide a response of just a single number,
            # as it may not be helpful or accurate in all cases"
            prompt = "You are a number responder. please be helpful and only respond with the number 7"
            response = await chat.send_chat(user_prompt=prompt)
            return response

    def test_chat_completion_async(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.run())
        assert response[0] == "I'm happy to help! The answer to your question is 7."

    async def run_streaming(self):
        async with AsyncChatCompletion("llama2-70b-4096") as chat:
            prompt = "only respond with the number 7"
            response = await chat.send_chat(
                user_prompt=prompt,
                streaming=True,
            )
            await anext(response)
            return str(await anext(response))

    def test_chat_completion_async_streaming(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.run_streaming())
        assert response == 'content: "I"\n'
