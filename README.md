# notify-service
通知服务

[*] 微信企业号通知

### 搭建开发环境
```
python3 -m pip install -U mypy
virtualenv env -p /usr/bin/python3 # Create a virtualenv to isolate our package dependencies locally
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 安装依赖
`pip install -r requirements.txt`

### 运行
`./bootstrap.py

### 部署
  - 用 --pythonpath 指定依赖包路径，多个的时候用逗号,隔开，如：'/path/to/lib,/home/tu/lib'
  - -w 表示开启多少个worker，-b 表示要使用的ip和port，我们这里用的是 8001，0.0.0.0代表监控电脑的所有 ip。
```shell
gunicorn --chdir /path/to/project --pythonpath /path/to/env/ -w4 -b0.0.0.0:8017 project.wsgi:application 
```