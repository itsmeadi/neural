#neural without training
import numpy as np
class neural:
	def __init__(self):
		np.random.seed(1)
		self.hl=3
		self.il=2
		self.ol=1
		self.w1=np.random.randn(self.il,self.hl)
		self.w2=np.random.randn(self.hl,self.ol)
	def forward(self,X):
		self.z2=np.dot(X,self.w1)
		self.a2=self.sigmoid(self.z2)
		self.z3=np.dot(self.a2,self.w2)
		return self.z3
	def sigmoid(self,x):
		return 1/(1+np.exp(-x))
	def sig_d(self,x):
		e=np.exp(-x)
		return -e/(1+e)**2
	def forward_train(self,X,y):
		r=self.forward(X)
		diff=y-r
		delta3=np.multiply(-diff,self.sig_d(self.z3))
		dJdW2=np.dot(self.a2.T,delta3)
		delta2=np.dot(delta3,self.w2.T)*self.sig_d(self.z2)
		dJdW1=np.dot(X.T,delta2)
		return dJdW2,dJdW1

		
n=neural()
a=np.array(([3,5],[5,1],[10,2]),dtype=float)
tst=np.array(([75],[82],[93]),dtype=float)
ans=n.forward(a)
c1,c2=n.forward_train(a,tst)
print ans

print c1
print "\n",c2
