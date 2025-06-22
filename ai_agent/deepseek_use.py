import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('DEEPSEEK_API_KEY')
openai = OpenAI(api_key=api_key,
                base_url="https://api.deepseek.com/v1")  # api_key is your DeepSeek API Key,base_url is your DeepSeek API Address

# A class to represent a Webpage
# If you're not familiar with Classes, check out the "Intermediate Python" notebook

# Some websites need you to use proper headers when fetching them:
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)


def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt


def messages_for(website):
    system_prompt = "You are an assistant that analyzes the contents of a website \
    and provides a short summary, ignoring text that might be navigation related. \
    Respond in markdown in Chinese."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]


def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=messages_for(website)
    )
    return response.choices[0].message.content


def display_summary(url):
    summary = summarize(url)
    # display(Markdown(summary))
    print(summary)


display_summary("https://edwarddonner.com")

"""
```markdown
# 爱德华·唐纳个人网站摘要

## 关于
- 爱德华·唐纳（Ed）是Nebula.io的联合创始人兼CTO，专注于利用AI帮助人们发掘潜力并实现人生目标。
- 此前创立AI初创公司untapt，该公司于2021年被收购。
- 兴趣包括编程、LLM实验、DJ（业余）、电子音乐制作（非常业余）以及浏览Hacker News。

## 专业背景
- Nebula.io的产品应用于人才招聘领域，使用专有LLM技术，并拥有专利匹配模型。
- 平台获得奖项，客户反馈积极，并有大量媒体报道。

## 最新动态（2025年）
1. **5月28日**: 推出课程《成为LLM专家和领导者》
2. **5月18日**: 发布《2025年AI高管简报》
3. **4月21日**: 推出《完整的Agentic AI工程课程》
4. **1月23日**: 举办《LLM Workshop – Hands-on with Agents》并提供资源

## 其他项目
- **Connect Four**: 未具体描述
- **Outsmart**: 一个让LLM在外交和策略上对抗的竞技场

## 联系方式
- 邮箱: ed [at] edwarddonner [dot] com
- 社交媒体: LinkedIn, Twitter, Facebook
- 可订阅新闻通讯
```
"""