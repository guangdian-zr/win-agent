# Win-Agent 文档

## 项目简介
Win-Agent 是一个基于浏览器的智能代理工具，用于自动化网页操作和信息获取。当前版本专门用于比较不同AI模型（如GPT-4o和DeepSeek-V3）的价格信息。

## 快速开始

### 环境配置
创建 `.env` 文件并配置以下参数：
```
API_KEY=your_api_key_here
API_URL=your_api_base_url
MODEL=glm-4.5
```

### 安装依赖
```bash
pip install browser_use python-dotenv
```

### 运行程序
```bash
python main.py
```

## 功能特性
- 自动化浏览器操作
- AI模型价格比较
- 支持多种LLM后端
- 环境变量配置管理

## 技术栈
- Python 3.13+
- browser_use
- OpenAI API兼容接口
- asyncio异步编程

项目采用异步架构，通过browser_use库实现浏览器自动化，支持灵活的LLM配置。