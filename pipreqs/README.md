# 查找Python项目依赖并生成requirements.txt

安装 pipreqs 并更新
> pip install -U pipreqs

进入项目目录，执行
> pipreqs ./

自动在当前目录生成requirements.txt文件。

这个工具的好处是可以通过对项目目录的扫描，发现项目使用了哪些类库，自动生成依赖清单。

缺点是可能会有些偏差，需要检查并自己调整一下。
