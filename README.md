# 简介
欢迎使用智文文件助手。  
主要是通过迭代对excel拆分、合并、excel&csv格式转换，通过附件发送通过邮件等。
# 功能实现
## excel助手
通过xlrd、csv读取excel表格文件，通过对list按元素作为key分组或将不同list合并等方式，最后通过xlsxwriter写入excel文件  
举个栗子  
>        城市	学校	姓名	成绩  
>        北京	1中	张三	45  
>        北京	2中	李四	42  
>        北京	3中	王五	43  
>        天津	6中	小亮	96  
>        天津	7中	小丽	108  
>        天津	1中	如花	120  
>        保定	4中	贝贝	156  
>        保定	5中	哈哈	168   
>        保定	7中	菜菜	192  
>        保定	1中	饭饭	205  
如果按照第一列城市拆分，则按照每行城市的名称拆分出**北京、天津、保定**三个文件。
## 邮件助手
对附件按文件名字符分成不同组织，和收件人列表recipients.txt映射，如果recipients.txt存在组织收件人，发送到对应的收件人，同时对发送失败的附件发送到发件人邮箱
# 使用准备
## 修改配置文件sf_config.ini
**sf_config.ini**是读取、操作文件的路径信息,需写入绝对路径,可直接从文件夹复制(如路径存在)，书写请按照*D:\smartfile\file*样式

**separator**是文件拆分和邮件助手判定组织的分隔符号。  
如分隔符号为❤,依旧以上述栗子,拆分后文件为"城市❤成绩单.xlsx";同样,在使用邮件助手时,附件如果含有❤则按以❤之前的文字作为收件组织，如"北京❤成绩单.xlsx"发给北京对应收件人.如果文件无❤,如"关于下发成绩的通知.docx",则为公共附件,发送给所有收件人.  
ps:**分隔符不建议使用常用标点和.号，容易出现误伤**
## 执行.bat文件,安装python和相关模块
双击执行.bat文件，自动下载和安装python文件，如果sf_config.ini配置的文件夹路径不存在，创建文件夹
仅需第一次安装时使用
## 修改配置文件sender.ini和recipients.txt(仅限邮件助手使用)
# 使用方法
