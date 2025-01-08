"""
LinkedIn Harvard graduates search example.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='''Go to linkedin.com, log in using email: goose5620@topvu.net and password: damuswatest.
	After logging in, search for "Julian Saks", click on the first profile that appears,
	and return detailed information from their LinkedIn bio and profile.''',
	llm=llm,
)

async def main():
	await agent.run(max_steps=15)
	agent.create_history_gif()

if __name__ == "__main__":
	asyncio.run(main())
