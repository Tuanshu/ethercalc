import requests


# GET: http://localhost:81/_/otd4vhbpd4bh/cells/B3
def update_ethercalc_cell(sheet_name, cell, value):
    # 指定 EtherCalc 服務的 URL
    url = f'http://localhost:81/_/{sheet_name}/'

    # 創建要發送的命令，例如 "set A1 text value"
    # command = f'set {cell} text {value}'
    command = [f'set {cell} text t {value}']

    # 發送 POST 請求
    response = requests.post(url, json={'command': command})

    # 檢查響應
    if response.status_code == 202:
        print("成功更新單元格")
    else:
        print("更新失敗", response.status_code)


# 使用示例：將 my_spreadsheet 表格中的 A1 單元格更新為 "Hello"
update_ethercalc_cell('mysheet', 'C9', 'hi \n1. \n2. \n3.')
