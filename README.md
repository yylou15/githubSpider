# githubSpider
爬取github用户信息及所有代码包

本项目基于Scrapy 1.5.1和Python 3.7，可以实现爬取某个用户所有项目的基本信息（保存在csv文件中）和下载所有代码包（zip）
使用说明：
1.安装Scrapy，用pip命令如下：
    pip install scrapy
  正确安装完成后安装完成后输入scrapy可以看到：
  
    Scrapy 1.5.1 - project: github

    Usage:
      scrapy <command> [options] [args]

    Available commands:
      bench         Run quick benchmark test
      check         Check spider contracts
      crawl         Run a spider
      edit          Edit spider
      fetch         Fetch a URL using the Scrapy downloader
      genspider     Generate new spider using pre-defined templates
      list          List available spiders
      parse         Parse URL (using its spider) and print the results
      runspider     Run a self-contained spider (without creating a project)
      settings      Get settings values
      shell         Interactive scraping console
      startproject  Create new project
      version       Print Scrapy version
      view          Open URL in browser, as seen by Scrapy

    Use "scrapy <command> -h" to see more info about a command
    
2.为了运行本项目，下载本项目并解压，打开命令行窗口，cd至对应目录  your/path/to/githubSpider

3.输入命令scrapy crawl githubSpider 运行爬虫
    注：为了将项目的信息保存在表格中，请在命令最后加上 -o <文件名>.csv
          如scrapy crawl githubSpider -o test.csv
          
          
4.根据提示，输入github用户的id，即可自动运行，运行完成后，csv文件保存在当前目录，即your/path/to/githubSpider，
  该用户的所有项目代码包保存在  your/path/to/githubSpider/Downloads/<用户id>  文件夹下

注：Scrapy和Python3并不能完美兼容，如果在安装或使用Scrapy的过程中出现任何问题，尝试百度解决吧~
