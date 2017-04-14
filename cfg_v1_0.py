
# coding: utf-8

# In[37]:

from pynq import Overlay
from pynq import PL
from pynq import MMIO

OL = Overlay("cfg_v1_0.bit")
OL.download()

OL.is_loaded()


# In[38]:

BASE_ADDRESS = 0x43C00000
adder_ip = MMIO(0x43C00000,0x10000)
adder_ip.write(0)
adder_ip.write(1)
adder_ip.write(1)
adder_ip.write(0)
adder_ip.write(1)

adder_ip.read(10)


# In[ ]:



