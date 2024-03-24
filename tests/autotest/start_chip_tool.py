import sys
import asyncio
import time
import json
import base64
import psutil
from websocket_runner import WebSocketRunner, WebSocketRunnerConfig

websocket_runner_config = WebSocketRunnerConfig(
    'localhost', 9002, './chip-tool', 'interactive server --storage-directory ./data')

runner = WebSocketRunner(websocket_runner_config)

def check_and_terminate_process(process_name):
    # 遍历当前所有进程
    for proc in psutil.process_iter():
        try:
            # 获取进程信息
            process_info = proc.as_dict(attrs=['pid', 'name'])
            # 检查进程名是否匹配目标进程名
            if process_info['name'] == process_name:
                print(f"Found process {process_name} with PID {process_info['pid']}. Terminating...")
                # 结束进程
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def start():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(runner.run())

def decode_logs(response):
    # 打印logs部分
    print("\nLogs:")
    for log in response['logs']:
        module = log['module']
        category = log['category']
        message = base64.b64decode(log['message']).decode('utf-8')
        print(f"[{module}][{category}]: {message}")

def decode_results(response):
    print("Results:")
    if 'results' in response and isinstance(response['results'], list):
        if any('error' in result and result['error'] == 'FAILURE' for result in response['results']):
            print("error: ", response['results'][0]["error"])
        else:
            for result in response['results']:
                print("attributeId: ", result["attributeId"])
                print("clusterId: ", result["clusterId"])
                print("dataVersion: ", result["dataVersion"])
                print("endpointId: ", result["endpointId"])
                print("value: ", result["value"])
    else:
        print("Unknown data formate")

def decodeResponse(response: str):
    response_dict = json.loads(response)
    decode_results(response_dict)
    decode_logs(response_dict)


if __name__ == '__main__':
    success = True
    check_and_terminate_process("chip-tool")

    try:
        start()
        while(1):
            if runner.is_connected == False:
                print("The client is not connected")
                time.sleep(1)
            else:
                print("The client is connected")
                loop = asyncio.get_event_loop()
                # encoded_response = loop.run_until_complete(runner.execute("basicinformation read vendor-name 111 0"))
                encoded_response = loop.run_until_complete(runner.execute("descriptor read server-list 111 0"))
                decodeResponse(encoded_response)
                time.sleep(3)

    except KeyboardInterrupt:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(runner.stop())
        print("Exit !")
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Caught an unexpected exception: {e}")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(runner.stop())
