# flask-demo
flask demo

Windows 安装配置环境
# 安装
# 下载 https://bitbucket.org/pypa/setuptools  安装脚本  (ez_setup.py) (move to https://github.com/pypa/setuptools)
$ python ez_setup.py

# 添加Python/Scripts 文件夹(C:\Python27\Scripts)到环境变量Path中
# 可能需要重启命令提示符才能使用刚刚配置的命令

# 安装 virtualenv
$ easy_install virtualenv

# 初始化虚拟环境
$ virtualenv venv

# 激活虚拟环境
$ venv\Scripts\activate

# 根据 requirements.txt 安装依赖包
$ pip install -r requirements.txt

# 根据当前环境生成 requirements.txt
$ pip freeze > requirements.txt

# 退出虚拟环境
$ deactivate

Mac 安装配置环境
# 安装python virtualenv, 可以安装虚拟环境，可以配置的python,django等版本不容易导致版本冲突问题
# 此处需要超级管理员权限，否则安装失败
$ sudo pip install virtualenv

# 安装成功之后，回到cd
# 创建一个名为 venv 的虚拟环境，当然目录建议放到/home/
$ virtualenv venv

# 启动 virtualenv
$ source venv/bin/activate

# 启动应用
$ python app.py

# 使用这个虚拟环境下面，安装需要的开发工具
$ python install Django==1.6.1

# 当然这里推荐先
$ git clone https://github.com/django/django.git
# 这种方式下载速度快很多，毕竟github拥有更多的带宽资源

# 推出退出虚拟环境的命令
$ deactivate
