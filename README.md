# Microsoft AutoGen + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/autogen-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/autogen-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable Microsoft AutoGen examples using the official [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent) executor.

> Examples only: no separately published `autogen-capsolver` package or duplicated SDK.

## Repository scope

The demo maps shared async CapSolver operations to AutoGen `FunctionTool` instances. AutoGen owns the agent loop; CapSolver Agent owns tool execution.

## Quick start

```bash
git clone https://github.com/capsolver-ai/autogen-capsolver.git
cd autogen-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Export [`.env.example`](.env.example) values and run `python examples/quickstart.py`.

## Key integration code

```python
from autogen_core.tools import FunctionTool
from capsolver_agent import create_executor

capsolver = create_executor()

async def get_capsolver_balance() -> str:
    return str(await capsolver.execute("get_balance", {}))

tool = FunctionTool(get_capsolver_balance, description="Return the CapSolver balance.")
```

See [`examples/quickstart.py`](examples/quickstart.py) for the complete `AssistantAgent` flow.

## Project layout

```text
examples/quickstart.py   AutoGen AssistantAgent and FunctionTools
requirements.txt         Shared SDK repositories plus AutoGen
tests/test_demo.py        Offline validation
.github/workflows/ci.yml  Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver for AI agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [AutoGen tools](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html)

## Responsible use

Use the example only for lawful, user-authorized workflows that respect target-site terms. Never commit secrets or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

AutoGen is a third-party project. This repository is maintained by CapSolver and is not affiliated with or endorsed by Microsoft.
