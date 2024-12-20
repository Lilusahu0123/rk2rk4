#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib import pyplot as plt
t_ini=0
t_ter=1
n=input('number of iteration=')
n=int(n)
h=(t_ter-t_ini)/n
def fun1(t,u,v):
    return v
def fun2(t,u,v):
    return -np.sin(u)
t=np.arange(t_ini,t_ter+h,h)
u=np.zeros(n+1)
v=np.zeros(n+1)
u[0]=1
v[0]=0
for i in range(n):
    k1=fun1(t[i],u[i],v[i])
    l1=fun2(t[i],u[i],v[i])
    k2=fun1(t[i]+h/2,u[i]+h*k1/2,v[i]+h*l1/2)
    l2=fun2(t[i]+h/2,u[i]+h*k1/2,v[i]+h*l1/2)
    k3=fun1(t[i]+h/2,u[i]+h*k2/2,v[i]+h*l2/2)
    l3=fun2(t[i]+h/2,u[i]+h*k2/2,v[i]+h*l2/2)
    k4=fun1(t[i]+h,u[i]+h*k3,v[i]+h*l3)
    l4=fun2(t[i]+h,u[i]+h*k3,v[i]+h*l3)
    u[i+1]=u[i]+h*(k1/6+k2/3+k3/3+k4/6)
    v[i+1]=v[i]+h*(l1/6+l2/3+l3/3+l4/6)
plt.plot(t, u, '.:', color='purple', label="Runge-Kutta method 4th order")

u=np.zeros(n+1)
v=np.zeros(n+1)
u[0]=1
v[0]=0
for i in range(n):
    k1=fun1(t[i],u[i],v[i])
    l1=fun2(t[i],u[i],v[i])
    k2=fun1(t[i]+h,u[i]+h*k1,v[i]+h*l1)
    l2=fun2(t[i]+h,u[i]+h*k1,v[i]+h*l1)
    u[i+1]=u[i]+h*(k1+k2)/2
    v[i+1]=v[i]+h*(l1+l2)/2
plt.plot(t, u, '+:', color='red', label="Runge-Kutta method 2nd order")    
plt.title('Runge-Kutta Method')
plt.xlabel('t', fontsize=15)
plt.ylabel('u(t)', fontsize=15)
plt.grid()
plt.show()         
         
         
         
         
         
    
    


# In[ ]:




