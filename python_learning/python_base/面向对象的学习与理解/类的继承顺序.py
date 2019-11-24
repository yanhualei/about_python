class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print( "stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print( "stop C stop!")

class D(B,C):
    def go(self):
        super(D,self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print( "stop D stop!")
    def pause(self):
        print ("wait D wait!")

if __name__ == '__main__':
    d=D()
    d.go()
    d.stop()
    d.pause()

# 这个实例验证了python3类的继承是广度优先
#  所以类的检索顺序：DBCA，执行顺序ACBD