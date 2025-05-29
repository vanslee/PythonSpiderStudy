from lxml import etree
from pathlib import Path
text = '''
<div>
    <ul>
         <li class="li li-first"><a href="link.html">first item1</a></li> 
         <li class="li li-first" name="item"><a href="link.html">first item2</a></li>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
path = Path('lxml_test.html')
html = etree.HTML(text)
result = etree.tostring(html)
path.write_text(result.decode('utf-8'))
html = etree.parse('./lxml_test.html', etree.HTMLParser())
# 获取子孙节点
# result = html.xpath('//ul//a')
# 获取父节点
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# 属性匹配
# result = html.xpath('//li[@class="item-0"]')
# result = html.xpath('//li[@class="item-0"]//a/text()')
# 属性获取
# result = html.xpath('//li/a/@href')
# 属性多值
# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# 多属性匹配
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# 获取标签的所有属性
result = html.xpath('//li[1]/attribute::*')
print(result)
