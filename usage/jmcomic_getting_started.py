"""
--------------------
    API快速上手
--------------------
"""
import jmcomic  # 导入此模块，需要先安装.
jmcomic.download_album('195818')  # 传入要下载的album的id，即可下载整个album到本地.
# 上面的这行代码，还有一个可选参数option: JmOption，表示配置项，
# 配置项的作用是告诉程序下载时候的一些选择，
# 比如，要下载到哪个文件夹，使用怎样的路径组织方式（比如[/作者/本子id/图片] 或者 [/作者/本子名称/图片]）.
# 如果没有配置，则会使用 JmOption.default()，下载的路径是[当前工作文件夹/本子名称/图片].


"""
--------------------
    批量下载介绍
--------------------
"""
# 如果你想要批量下载，可以使用 list/set/tuple/生成器 作为第一个参数。
# 第二个参数依然是可选的JmOption对象
jmcomic.download_album(['195818', '1', '2', '3'])  # list
jmcomic.download_album({'195818', '1', '2', '3'})  # set
jmcomic.download_album(('195818', '1', '2', '3'))  # tuple
jmcomic.download_album(aid for aid in ('195818', '1', '2', '3'))  # 生成器

"""
--------------------
    配置文件介绍
--------------------
"""
# 先获取默认的JmOption对象
jm_option = jmcomic.JmOption.default()

# 可以把对象保存为yml文件，方便日后修改。保存格式会根据后缀名智能转换。
jm_option.save_to_file('./禁漫下载默认配置.yml')  # yml格式，推荐
jm_option.save_to_file('./禁漫下载默认配置.json')  # json格式

# 如果你修改了默认配置，现在想用你修改后的配置来下载，使用如下代码
jm_option = jmcomic.create_option('./禁漫下载默认配置.yml')
jmcomic.download_album('195818', jm_option)
