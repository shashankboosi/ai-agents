import asyncio
import os

from browser_use import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatOpenAI(
            model="gpt-4o", temperature=0, api_key=os.getenv("OPENAI_API_KEY")
        ),
    )
    result = await agent.run()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
