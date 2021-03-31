## 用户登录和注册项目

## 简单使用方法
##### 创建虚拟环境
##### 使用pip安装第三方依赖
##### 修改settings_example.py文件为settings.py
##### 运行migrate命令，创建数据库和表
##### 运行python3 manager.py runserver 0:port 启动服务器


##### 路由设置
##### from django.contrib import admin
##### from django.urls import path, include
##### from login import views

##### urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls'))   # 增加这一行
##### ]


my_website - User login and register system

   Copyright 2021- www.yueminghai.top

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.