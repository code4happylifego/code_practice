import json
import os
import requests
from dotenv import load_dotenv
import urllib.request
import time
load_dotenv()


class DeepSeekAgent:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

        # 扩展工具库（可自定义添加）
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "calculator",
                    "description": "计算一个数学表达式并返回结果，支持加减乘除等基本运算。",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "数学表达式，例如：2+3 * 4"
                            }
                        },
                        "required": ["expression"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "reverse_string",
                    "description": "反转一个字符串",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "要反转的字符串"
                            }
                        },
                        "required": ["text"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "website_response_time",
                    "description": "探测指定网站的响应时间（单位：毫秒），检测网站可用性",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "需要检测的完整网站URL，必须包含协议前缀（如 https://）",
                                "pattern": "^https?://.+"
                            }
                        },
                        "required": ["url"]
                    }
                }
            }
        ]

    def chat(self, messages):
        """调用DeepSeek对话接口"""
        data = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 500,
            "tools": self.tools
        }
        res = requests.post(self.api_url, json=data, headers=self.headers)
        response_json = res.json()
        print(response_json)

        return response_json

    # 示例工具1：数学计算
    def calculate(self, expr):
        try:
            result = eval(expr)  # 实际项目建议用safe_eval库
            return f"计算结果: {expr} = {result}"
        except:
            return "计算失败！请检查表达式"

    # 示例工具2：字符串反转
    def reverse_string(self, text):
        return f"反转结果: {text[::-1]}"

    def website_response_time(self, url):
        """
        探测网站响应时间
        :param url:
        :return:
        """
        try:
            start_time = time.time()
            _ = urllib.request.urlopen(url, timeout=5)
            end_time = time.time()
            elapsed = (end_time - start_time) * 1000  # 转换为毫秒
            return f"响应时间: {elapsed:.2f} ms"
        except Exception as e:
            return f"请求异常: {e}"

    def run(self):
        history = []  # 保存对话记忆
        while True:
            user_input = input("👤 你: ")
            if user_input.lower() == "exit":
                break

            history.append({"role": "user", "content": user_input})
            response_json = self.chat(history)
            ai_response = response_json["choices"][0]["message"]
            # 工具调用检测
            if "tool_calls" in ai_response:
                history.append(ai_response)
                tool_call = ai_response["tool_calls"][0]
                func_name = tool_call['function']['name']
                args = json.loads(tool_call['function']['arguments'])

                # 执行工具函数
                if func_name == "calculator":
                    tool_result = self.calculate(args['expression'])
                elif func_name == "reverse_string":
                    tool_result = self.reverse_string(args['text'])
                elif func_name == "website_response_time":
                    tool_result = self.website_response_time(args['url'])
                else:
                    tool_result = f"未识别的工具函数：{func_name}"

                # 将工具结果加入对话历史
                history.append({
                    "role": "tool",
                    "content": tool_result,
                    "tool_call_id": tool_call.get("id","")
                })

                # 二次调用API生成最终回复
                final_response = self.chat(history)
                print(f"🤖 Agent: {final_response['choices'][0]['message']['content']}")
                final_message = final_response['choices'][0]['message']
                history.append(final_message)
            else:
                print(f"🤖 Agent: {ai_response['content']}")


if __name__ == "__main__":
    agent = DeepSeekAgent()
    agent.run()

"""
👤 你: 计算 28* 89
{'id': 'a58cdc6c-d938-4d0a-a6bc-5af8a36a85a3', 'object': 'chat.completion', 'created': 1749390006, 'model': 'deepseek-chat', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': '', 'tool_calls': [{'index': 0, 'id': 'call_0_b82171be-2464-4fdf-9533-cedbc7077840', 'type': 'function', 'function': {'name': 'calculator', 'arguments': '{"expression":"28*89"}'}}]}, 'logprobs': None, 'finish_reason': 'tool_calls'}], 'usage': {'prompt_tokens': 337, 'completion_tokens': 20, 'total_tokens': 357, 'prompt_tokens_details': {'cached_tokens': 320}, 'prompt_cache_hit_tokens': 320, 'prompt_cache_miss_tokens': 17}, 'system_fingerprint': 'fp_8802369eaa_prod0425fp8'}
{'id': '2a15c28e-fc19-44b4-b137-3ff8c1bbf3ad', 'object': 'chat.completion', 'created': 1749390011, 'model': 'deepseek-chat', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': '28乘以89等于2492。'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 371, 'completion_tokens': 7, 'total_tokens': 378, 'prompt_tokens_details': {'cached_tokens': 320}, 'prompt_cache_hit_tokens': 320, 'prompt_cache_miss_tokens': 51}, 'system_fingerprint': 'fp_8802369eaa_prod0425fp8'}
🤖 Agent: 28乘以89等于2492。
👤 你: 统计当前baidu.com的响应时间
{'id': '6e5d234b-6e76-46b7-8cb3-7a941098391e', 'object': 'chat.completion', 'created': 1749390031, 'model': 'deepseek-chat', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': '', 'tool_calls': [{'index': 0, 'id': 'call_0_4f956b0c-018b-433a-ab76-e7346044a972', 'type': 'function', 'function': {'name': 'website_response_time', 'arguments': '{"url":"https://www.baidu.com"}'}}]}, 'logprobs': None, 'finish_reason': 'tool_calls'}], 'usage': {'prompt_tokens': 389, 'completion_tokens': 24, 'total_tokens': 413, 'prompt_tokens_details': {'cached_tokens': 320}, 'prompt_cache_hit_tokens': 320, 'prompt_cache_miss_tokens': 69}, 'system_fingerprint': 'fp_8802369eaa_prod0425fp8'}
{'id': 'd695ca73-99c8-4463-a0d3-68db7b627063', 'object': 'chat.completion', 'created': 1749390036, 'model': 'deepseek-chat', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': '当前访问百度（baidu.com）的响应时间为 **104.99 毫秒**。'}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 426, 'completion_tokens': 20, 'total_tokens': 446, 'prompt_tokens_details': {'cached_tokens': 384}, 'prompt_cache_hit_tokens': 384, 'prompt_cache_miss_tokens': 42}, 'system_fingerprint': 'fp_8802369eaa_prod0425fp8'}
🤖 Agent: 当前访问百度（baidu.com）的响应时间为 **104.99 毫秒**。
"""