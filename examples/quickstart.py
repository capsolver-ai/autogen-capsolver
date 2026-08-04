import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_capsolver import get_capsolver_tools


async def main() -> None:
    model = OpenAIChatCompletionClient(model="gpt-4.1-mini")
    agent = AssistantAgent("assistant", model_client=model, tools=get_capsolver_tools())
    print(await agent.run(task="Check my CapSolver balance."))


asyncio.run(main())
