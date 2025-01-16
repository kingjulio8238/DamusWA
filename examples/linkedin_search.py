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
	task='''Go to linkedin.com, log in using email: skipper72585@mailshan.com and password: damuswest5.
	After logging in, search for "Gabriele Ansaldo", click on the first profile that appears.
	Gather and return:
	- Detailed information from their LinkedIn bio and profile
	- A comprehensive list of all job experiences, including:
		- Company name
		- Job title
		- Employment duration
		- Job description/responsibilities if available
		- Location if available
	Make sure to scroll through the entire profile to capture all work history entries.''',
	llm=llm,
)

async def main():
	await agent.run(max_steps=15)
	agent.create_history_gif()

if __name__ == "__main__":
	asyncio.run(main())
