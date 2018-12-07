# flask web 项目的说明文档

## 描述

本项目是 flask 实现的一个web框架，项目结构仿照django实现， 需要 flask-blueprint
项目依赖包在requirement.txt中， 安装可以使用： python -m pip install -r requirement.txt 完成包安装。



## 运行项目：

* 项目采用 flask-script 来管理运行
	* 运行： python3 app.py runserver -h 0.0.0.0 -p 9000

* 项目采用 flask-sqlalchemy 来链接映射数据库
* 项目采用 flask-blueprint 管理划分不同的 module
* 项目采用 flask-restful 实现接口
* 项目采用 flask-migrate 构建 sqlalchemy 的迁移文件
