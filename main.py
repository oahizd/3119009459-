
import jieba

# 文本位置
with open(r'C:\Users\oahizd\Desktop\学习\软工\测试文本2\orig.txt',encoding='UTF-8') as read_file:
    filename1=read_file.read()
with open(r'C:\Users\oahizd\Desktop\学习\软工\测试文本2\orig_0.8_dis_10.txt',encoding='UTF-8') as read_file:
    filename2=read_file.read()


words1 = jieba.lcut(filename1, cut_all=True)
words2 = jieba.lcut(filename2, cut_all=True)


class simhash:

    # 构造函数
    def __init__(self, tokens='', hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    # toString函数
    def __str__(self):
        return str(self.hash)

    # 生成simhash值
    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]:  # t为token的普通hash值
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1  # 查看当前bit位是否为1,是的话将该位+1
                else:
                    v[i] -= 1  # 否则的话,该位-1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint

    # 求海明距离
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x - 1
        return tot

    # 求相似度
    def similarity(self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b

    # 生成hash值
    def _string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x


if __name__ == '__main__':
    s = words1
    hash1 = simhash(s)

    s = words2
    hash2 = simhash(s)

print(hash1.hamming_distance(hash2), "   ", hash1.similarity(hash2))

result = open(r'C:\Users\oahizd\Desktop\学习\软工\测试文本2\result.txt', 'a+', encoding='utf-8')

result.write(("相似率是：%.2f%%"  %(hash1.similarity(hash2)*100)))

result.close()


