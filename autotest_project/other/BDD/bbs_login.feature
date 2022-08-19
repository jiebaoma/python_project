#对测试过程的行为描述文档。Gherkin
  Feature: 功能描述，内网BBS论坛-登录功能
    下面的场景就是对于测试过程步骤的描述
    以下的描述可以由非测试人员编写  Feature、Scenario、Given、when
    通过特定的关键字：描述一个用户的操作行为

    Scenario: 场景1-正常登录
      #Given 数据定义
      Given 我有一个账户 用户名:admin 密码:admin
      #when 测试具体步骤
      When 打开这个登录页面
      And 输入用户名
      And 输入密码
      And 点击登录按钮

      #then 判断
      Then 判断页面中是否包含登出链接，如果没有表示登录失败
