#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Required package


# In[ ]:


# pip install firebase
# pip install requests
# pip install firebase_admin


# In[1]:


import pywhatkit
import requests
import math, random
from firebase import firebase
from firebase_admin import credentials, initialize_app, storage, firestore
cred = credentials.Certificate(r"serviceAccountKey.json")
initialize_app(cred, {'storageBucket': 'stock-data-fc41e.appspot.com'})
db = firestore.client()


# In[2]:


doc_ref = db.collection(u'user').document(u'data')
phnum = doc_ref.get(field_paths={'phone'}).to_dict().get('phone')

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
        doc_ref = db.collection(u'user').document(u'data')
        doc_ref.set({
        u'otp': OTP
        }, merge=True)
    return OTP
try:
    requests.post('https://whatsapp-node-api.herokuapp.com/chat/sendmessage/'+phnum, json={'message': 'Your OTP is '+generateOTP()})
    print("Successfully Sent!")
except:
    print("An Unexpected Error!")
