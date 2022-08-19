from BaseObject import SeleniumMethod

class BaiduPage(SeleniumMethod):
    # 百度页面对象

    inputBox = ".//*[@id='kw']"
    # 百度输入框
    searchBotton = ".//*[@id='su']"
    # 百度搜索按钮

    responseTitle = "中国_百度搜索"
    # 搜索结果页的标题
    oneResult = ".//*[@id='1']/h3/a"
    # 第一行
    oneResultText = "中国_百度百科"
    # 第一行的文本

    def searchChinese(self):
        # 搜索中国
        self.clearAndInput(self.inputBox, "中国")
        self.click(self.searchBotton)