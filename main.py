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
    
    # 自定义浏览器配置
    browser_config = {}
    
    # 支持自定义浏览器可执行文件路径
    custom_browser_path = os.getenv("BROWSER_EXECUTABLE_PATH")
    if custom_browser_path:
        browser_config["executable_path"] = custom_browser_path
    
    # 支持自定义浏览器类型 (chromium, firefox, webkit)
    browser_type = os.getenv("BROWSER_TYPE", "chromium")
    browser_config["browser_type"] = browser_type
    
    # 支持headless模式配置
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    browser_config["headless"] = headless
    
    agent = Agent(
        task="有多少个标签页",
        llm=ChatOpenAI(
            model=model,
            temperature=1.0,
            api_key=api_key,
            base_url=api_url
        ),
        browser_config=browser_config,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())