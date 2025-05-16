import requests

def get_website_content(url):
    """
    发送GET请求获取网页内容
    """
    response = requests.get(url)
    return {
        'status_code': response.status_code,
        'content': response.text,
        'headers': dict(response.headers)
    }

def post_data(url, data):
    """
    发送POST请求提交数据
    """
    response = requests.post(url, json=data)
    
    # 判断是否返回JSON数据
    if response.headers.get('Content-Type', '').startswith('application/json'):
        response_json = response.json()
    else:
        response_json = None
    return {
        'status_code': response.status_code,
        'response_json': response_json,
        'success': 200 <= response.status_code < 300
    }
    pass 