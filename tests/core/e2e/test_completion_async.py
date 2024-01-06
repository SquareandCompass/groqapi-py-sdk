import asyncio

from groq.cloud.core import AsyncCompletion


class TestCoreCompletionAsync:
    async def run(self):
        async with AsyncCompletion("llama2-70b-4096") as completion:
            prompt = "only respond with the number 7"
            response, id, stats = await completion.send_prompt(
                "llama2-70b-4096",
                user_prompt=prompt,
                system_prompt="only respond with the number 7",
            )
            return response

    def test_completion_async(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.run())
        assert response == "Sure! Here is my response:\n\n7"

    async def run_streaming(self):
        async with AsyncCompletion("llama2-70b-4096") as completion:
            prompt = "only respond with the number 7"
            response = await completion.send_prompt(
                "llama2-70b-4096",
                user_prompt=prompt,
                system_prompt="only respond with the number 7",
                streaming=True,
            )
            await anext(response)
            return str(await anext(response))

    def test_completion_async_streaming(self):
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.run_streaming())
        assert response == 'content: "Sure"\n'
