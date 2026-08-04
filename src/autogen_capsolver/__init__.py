from __future__ import annotations

import json

from autogen_core.tools import FunctionTool
from capsolver_agent.schema import create_executor


def get_capsolver_tools(api_key: str | None = None) -> list[FunctionTool]:
    executor = create_executor(api_key=api_key)

    async def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
        result = await executor.execute("solve_captcha", {
            "captcha_type": captcha_type, "website_url": website_url, "website_key": website_key,
        })
        return json.dumps(result)

    async def get_balance() -> str:
        return json.dumps(await executor.execute("get_balance", {}))

    return [
        FunctionTool(solve_captcha, description="Solve a CAPTCHA in an authorized workflow."),
        FunctionTool(get_balance, description="Get the CapSolver account balance."),
    ]

__version__ = "0.1.0"
