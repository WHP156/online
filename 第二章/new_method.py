from lxml import etree
xml="""
<book>
    <id>1</id>
    <id>2</id>
    <price id='10086'>撒比</price>
    <div>
        <id>热了</id>
    </div>
    <span>
        <id>热了2</id>
    </span>
</book>
"""
tree=etree.XML(xml)
#tree=etree.parse('xxx')提取文件
result=tree.xpath("/book//id/text()")
result1=tree.xpath("/book/*/id/text()")
print(result) 
print(result1)
print(tree.xpath("/book//id[1]/text()"))
print(tree.xpath("/book//id[2]/text()"))
print(tree.xpath("/book/price[@id='10086']/text()"))
result2=tree.xpath("/book//id")
for it in result2:
    print(it.xpath('./text()'))
result3=tree.xpath("/book/price/@id")
print(result3)