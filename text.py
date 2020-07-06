from lxml import etree
tree = etree.parse('a.html')
t = tree.xpath('/div[@class="ns_area list"]/ul/li')
print(t)