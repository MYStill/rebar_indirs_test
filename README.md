# rebar_indirs_test
对不起了,用中文写比较顺手

准备:

python3.7.6写的python脚本执行会创建一个目录层次比较深的rebar3项目，大约有14000文件和4480目录

本地16g内存试了下reba3 3.24.0 编译，内存会满

应该在类似D:aa/bb/cc/dd/ee/ff 比较深的路径下放rebar3项目 indirs的内存占用更大

补充:

本来想打印下内存大小的，但是我家里的电脑短时间编译不了rebar3,无法修改代码调试.

实际使用的项目在4000左右文件就已经会内存溢出了，但是单个文件大小会大
