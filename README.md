# python
## django demo（图书管理网站）
前期准备：安装 python3.7， pyCharm， mysql
工具使用：vue，nginx，django，mysql
### 需求分析：
1. 管理员用户
  - 登录/登出
  - 管理用户：包括增删改查
  - 管理图书：包括增删改查
  - 属性信息：编号（全局唯一，自动生成），姓名（必填），密码（必填），性别，年龄，住址，联系电话（必填）
2. 普通用户
  - 注册/注销
  - 登录/登出
  - 管理图书
    - 浏览或查找网站的图书
    - 购买图书
    - 充值（查看明细）
    - 管理已购买图书，增删改查
    - 管理购物车：增删改查
  - 属性信息：用户名（全局唯一，必填），密码（必填），账户余额，联系电话（必填）
3. 图书
  - 属性信息：名称（必填），价格，类别（数组），阅读人数，购买人数
### 功能设计
1. system 
  - 注册（registry）：用户注册新账
  - 注销（cancel）：用户注销账号
  - 登录（login）：用户登录系统
  - 登出（logout）：用户退出系统
  - 推送（recommend）：推送用户可能喜欢的书籍
### 功能实现
1. 登录（login）
  - 创建 system 模块：`python manage.py startapp system`
  - 配置请求路由: 将 127.0.0.1：8000/ 请求路由到 system 模块中（在项目的 *settings.py* 中配置）
  - 配置登录/登出请求： 在 *system-urls.py* 中配置 login/  logout/ 请求拦截
  - 创建 user 模块：`python manage.py startapp user`
  - 创建 AdminUser 和 CommonUser 模型
  > 在 user-models.py 中添加 AdminUser 和 CommonUser class，并继承 `django.models.Model`  
  > 修改项目 *settings.py* 中 `DATABASES` 配置
  > ```DATABASES = {
  >      'default': {
  >           'ENGINE': 'django.db.backends.mysql',
  >           'NAME': 'zl_system',
  >           'USER': 'root',
  >           'PASSWORD': '123456',
  >           'HOST': '122.112.180.208',
  >           'PORT': '3360',
  >      }
  >    }```
