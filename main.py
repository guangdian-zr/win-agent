import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm import ChatOpenAI


async def main():
    """Main function to run the browser agent."""
    load_dotenv()
    
    # Get environment variables
    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")
    model = os.getenv("MODEL", "glm-4.5")
    
    agent = Agent(
        task="有多少个标签页",
        llm=ChatOpenAI(
            model=model,
            temperature=1.0,
            api_key=api_key,
            base_url=api_url
        ),
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())