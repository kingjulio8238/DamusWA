"""
Polymarket geopolitics markets scraper.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_openai import ChatOpenAI

from browser_use import Agent

llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
	task='''Go to polymarket.com, click on the "Global Elections" category, and search for markets related to this category. For each relevant market found, collect and return:
	- Market title/question
	- Current prices for all outcomes 
	- Trading volume
	- Expiration date/time
	- Any other relevant market details displayed
	Compile the information into a detailed list.''',
	llm=llm,
)

async def main():
	await agent.run(max_steps=15)
	agent.create_history_gif()

if __name__ == "__main__":
	asyncio.run(main())
