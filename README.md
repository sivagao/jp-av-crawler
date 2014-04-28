# QUICK NOTE

## USAGE
- 安装依赖 pip install -r requirments.txt
- 安装mongodb, 并且启动`nohup mongod&`
- scrapy crawl jv_most_wanted_item (添加了download_delayer为1.2s左右，可以适当更改)

## 爬取的数据
- actor - 演员 type: list
- title - 片名 type: string
- category - 类型 type: list
- slug - 编号识别码 type: string
- downloadurl - magnet 下载地址 type: string `magnet link`
- preview - 封面 type: string `image src`

## 制定爬虫
- 到spiders目录中copy一份，然后修改
- SgmlLinkExtractor - 来提取要process的link(如果详情页)
- process handler - 具体的提取数据的handler(tips: scrapy shell <url>), 用hsx来xpath或正则去匹配要的数据


