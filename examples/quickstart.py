"""Wrap CapSolver Agent operations as Microsoft AutoGen FunctionTools."""

import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient
from capsolver_agent import create_executor


capsolver = create_executor()


async def get_capsolver_balance() -> str:
    return json.dumps(await capsolver.execute("get_balance", {}), ensure_ascii=False)


async def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
    result = await capsolver.execute(
        "solve_captcha",
        {
            "captcha_type": captcha_type,
            "website_url": website_url,
            "website_key": website_key,
        },
    )
    return json.dumps(result, ensure_ascii=False)


async def main() -> None:
    model_client = OpenAIChatCompletionClient(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    )
    agent = AssistantAgent(
        name="capsolver_demo",
        model_client=model_client,
        system_message=(
            "Use CapSolver only for lawful, user-authorized workflows. "
            "Never invent target details."
        ),
        tools=[
            FunctionTool(get_capsolver_balance, description="Return the current CapSolver balance."),
            FunctionTool(
                solve_captcha,
                description="Solve a supported CAPTCHA in an authorized workflow.",
            ),
        ],
    )
    result = await agent.run(
        task=os.getenv("DEMO_PROMPT", "Check my CapSolver balance and summarize it.")
    )
    print(result.messages[-1].content)
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
