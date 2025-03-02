import ssl
import time

from undetected_chromedriver import Chrome, ChromeOptions


def test_driver():
    url = 'https://www.javlibrary.com/cn/vl_searchbyid.php?keyword=IPX-177'
    # 测试使用，请求https网站时，禁用SSL证书验证
    ssl._create_default_https_context = ssl._create_unverified_context
    # 创建ChromeOptions对象，并设置一些选项
    options = ChromeOptions()
    # 如果要使用无界面访问，开启此参数，默认有窗口界面
    # options.add_argument('--headless')
    # 将窗口最大化
    options.add_argument('--start-maximized')
    options.add_argument('--disable-infobars')
    # 创建Chrome对象，并使用指定的选项启动Chrome浏览器
    driver = Chrome(options=options)
    # 如本地driver版本与浏览器版本不一致，使用executable_path 指定driver路径
    # driver = Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
    # 访问网站
    driver.get(url)
    time.sleep(15)
    page_source = driver.page_source

    print(page_source)


    # driver.refresh()
    # 关闭Chrome浏览器
    # driver.quit()


if __name__ == '__main__':
    test_driver()