import os

'''1.获取当前路径'''
dir_path = os.path.dirname(os.path.realpath(__file__))

'''2.路径拼接'''
os.path.join(dir_path, "path_2")