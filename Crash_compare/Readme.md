##ipa里面的framework以及对应版本读取
###一、读取配置表并下载dsym文件
####1、先使用compare_old_new.py对比上个版本的framework是否更新，如果没有或者少量更新（比如少于3个）则单独更新下载
"biu -d JDDBaseModule_1.1.12"

####2、如果更新较多或者首次配置，则使用get_frameworks_version.py 生成framework_list，批量下载

"biu -dsym"

###二、压缩成.zip
