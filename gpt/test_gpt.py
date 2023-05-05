#coding = utf-8
import openai
import os

def get_completion(prompt, model="gpt-3.5-turbo"):
    # 从环境变量中获取API密钥
    api_key = os.environ.get("OPENAI_API_KEY")

    # 如果找不到API密钥，给出提示
    if api_key is None:
        raise ValueError("请在环境变量中设置OPENAI_API_KEY")

    # 使用API密钥配置OpenAI库
    openai.api_key = api_key

    # 创建一个消息列表，包含用于与ChatGPT互动的输入消息
    messages = [{"role": "user", "content": prompt}]

    # 调用OpenAI API
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    # 从响应中提取回复
    message = response.choices[0].message['content'].strip()
    print(message)
    return message

# 使用示例
input_text = "你好，ChatGPT！"
completion = get_completion(input_text)
print("ChatGPT回复：", completion)
