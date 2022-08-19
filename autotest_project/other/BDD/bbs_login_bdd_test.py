#根据 行为描述文档而编写
from pytest_bdd import given,parsers,when,then

#和Given 行为 【数据的定义】
@given(parsers.parse("我有一个账户 用户名:{username} 密码:{password}"),target_fixture="user")
def user(username,password):
    return dict(username=username,password=password)

#对应一个行为
@when(parsers.parse("打开这个登录页面 {url}"))
def go_to_url(url,browser):
    browser.get(url)

#输入用户名
@when("输入用户名")
def input_username(browser,user):
    pass