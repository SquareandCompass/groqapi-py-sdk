#!/usr/bin/env python3

import asyncio
import os

from groq.cloud.core import AsyncChatCompletion, AsyncCompletion


async def run():
    async with AsyncCompletion("llama2-70b-4096") as completion:
        prompt = "What are transformers in machine learning?"
        response, id, stats = await completion.send_prompt(
            "llama2-70b-4096", user_prompt=prompt
        )
        if response != "":
            print(f"\nPrompt: {prompt}\n")
            print(f"Request ID: {id}")
            print(f"Output:\n {response}\n")
            print(f"Stats:\n {stats}\n")

    async with AsyncCompletion("llama2-70b-4096") as complstream:
        prompt = "What is the difference between ray tracing and path tracing?"
        response = await complstream.send_prompt(
            "llama2-70b-4096", user_prompt=prompt, streaming=True
        )
        print(f"\nPrompt: {prompt}\nStream Output:\n")
        output = ""
        async for resp in response:
            output += resp.content
        print(output)

    async with AsyncChatCompletion("llama2-70b-4096") as chat:
        prompt = "Who won the world series in 2020?"
        response = await chat.send_chat(prompt, streaming=True)
        print(f"Question : {prompt}\nResponse :\n")
        output = ""
        async for resp in response:
            output += resp.content
        print(output)
        prompt = "The Los Angeles Dodgers won the World Series in 2020."
        response = await chat.send_chat(prompt, streaming=True)
        print(f"Question : {prompt}\nResponse :\n")
        output = ""
        async for resp in response:
            output += resp.content
        print(output)
        prompt = "Where was it played?"
        response = await chat.send_chat(prompt, streaming=True)
        print(f"Question : {prompt}\nResponse :\n")
        output = ""
        async for resp in response:
            output += resp.content
        print(output)


if __name__ == "__main__":
    asyncio.run(run())
