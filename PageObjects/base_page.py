'''
Author: jiayb
Date: 2021-09-09 16:00:00
LastEditTime: 2021-09-09 17:21:16
FilePath: \test-by-unittest\PageObjects\base_page.py
Description: 基于selenium的二次封装
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_():
    """打开浏览器

    Returns:
        object: 返回driver对象
    """
    drvier = webdriver.Chrome()
    return drvier


class BasePange(object):
    """基于selenium二次封装

    """
    def __init__(self):
        """接受open_()的返回值，传递到类的内部"""
        self.driver = open_()

    def open_url(self, url):
        """访问url

        Args:
            url (str): 访问的地址路径
        """
        self.driver.get(url)

    def page_close(self):
        """关闭当前页面

        """
        self.driver.close()

    def quit(self):
        """关闭浏览器
        """
        self.driver.quit()

    def stop(self, second):
        """停止等待

        Args:
            second (float)): 输入等待时间
        """
        time.sleep(second)

    def max_size(self):
        """窗口最大化
        """
        self.driver.maximize_window()

    def set_size(self, width, height):
        """设置窗口大小

        Args:
            width (float): 宽度
            height (float): 长度
        """
        self.driver.set_window_size(width, height)

    def locator_(self, funs, value):
        """获取元素定位

        Args:
            funs (object)): 获取元素的方法
            value (str): 定位的值

        Returns:
            object:返回一个对象进行下一步操作
        """
        element = self.driver.find_element(funs, value)
        return element


if __name__ == '__main__':
    test = BasePange()
    test.open_url('https://www.baidu.com')
    # test.max_size()
    # test.set_size(400.1, 400)
    test.stop(0.5)
    test.input_(By.ID, 'kw', 'python')
    test.stop(5)
    test.quit()