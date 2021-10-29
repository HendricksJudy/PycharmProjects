# 序列化——pickle

import pickle

'''
序列化的目的是利于网络通信
pickle 模块提供的函数
        dumps() 序列化： 可以把一个python的任意对象序列化成为一个二进制
        loads() 反序列化：可以把一个序列化成二进制后的数据反序列化为python的对象
        
        dump(序列化对象，写入文件对象) 序列化一个数据对象并写入一个文件
        load(文件对象) 在一个文件中读取序列化数据，并完成反序列化
'''

vars1 = 'i love you'
vars2 = [1, 2, 3, 4]

# 使用 pickle.dumps 进行序列化成为一个二进制数据

varsser1 = pickle.dumps(vars1)
print(varsser1, type(varsser1))  # b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00\x8c\ni love you\x94.' <class 'bytes'>

varsser2 = pickle.dumps(vars2)
print(varsser2, type(varsser2))  # b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04e.' <class 'bytes'>

# 使用 loads 实现反序列化
antiser1 = pickle.loads(varsser2)
print(antiser1, type(antiser1))  # [1, 2, 3, 4] <class 'list'>


