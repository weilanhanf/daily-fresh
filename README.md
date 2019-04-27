## DailyFresh

**天天生鲜**：小型电商购物网站，基于<code>Python3.x</code>和<code>Django2.x</code>

项目尽量使用Django内部提供的API，后台管理为Django自带的管理系统django-admin。适合Django的小型实战项目。

## 功能简介：

- 商品浏览：商品的图片，售价，种类，简介以及库存等信息。
- 全文检索：支持对商品种类以及商品名称，简介的检索。
- 登录注册：用户的登录与注册。
- 用户中心：支持用户个人信息，收货地址等信息的更新，商品加入购物车，订单生成。
- 商品下单：在支付接口和企业资质的支持下可完成商品的下单功能，按照原子事务处理，下单异常则终止此次下单过程。
- 后台管理：支持后台管理功能，商品及用户信息的增加，更新与删除，可自定制样式与功能，日志，以及权限的管理和分配。


## 在线样例：

### 在线地址

[http://39.108.176.210](http://39.108.176.210)

账号：weilanhanf

密码：weilanhanf

### 管理人员入口

[http://39.108.176.210/admin](http://39.108.176.210/admin)

账号：root

密码：rootroot


## 预览：
### 首页
![index](https://raw.githubusercontent.com/weilanhanf/Photos/master/DailyFresh/index.png)

### 登录
![login](https://raw.githubusercontent.com/weilanhanf/Photos/master/DailyFresh/login.png)

### 商品详情
![goods](https://raw.githubusercontent.com/weilanhanf/Photos/master/DailyFresh/goods.png)

### 购物车
![cart](https://raw.githubusercontent.com/weilanhanf/Photos/master/DailyFresh/cart.png)

## 安装：

### 依赖包安装

下载文件进入项目目录之后，使用pip安装依赖包

<code>pip install -Ur requirements.txt</code>

### 数据库配置

数据库默认使用<code>Django</code>项目生成时自动创建的小型数据库<code>sqlite</code>

也可自行配置连接使用MySQL

### 创建超级用户

终端下执行:

<code>./python manage.py createsuperuser</code>

然后输入相应的超级用户名以及密码，邮箱即可。

### 开始运行

终端下执行:

<code>./python manage.py runserver</code>

浏览器打开: <code>http://127.0.0.1</code> 即可进入普通用户入口

浏览器打开: <code>http://127.0.0.1/admin</code> 即可进入超级用户入口


## 补充：

### 功能：

欢迎您对该项目做出任何补充与修改：
- 商品的评价功能
- 合适的商品推荐算法
- 用户的邮箱注册
- 一个更多商品数据量的数据库
</br>
......
</br>
最近一段时间比较忙，以后会慢慢完善

## 感谢：

感谢您的star

### 联系：

如需联系请前往博客园留言 <a href="https://www.cnblogs.com/welan/p/9231530.html" target="_blank">蔚蓝的蓝</a>
