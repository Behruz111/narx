import streamlit as st
import sklearn
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np



m = pickle.load(open("model.pkl", "rb"))


def pre(kiruvchidata):
    i = np.array(kiruvchidata)

    ir = i.reshape(1, -1)
    p = m.predict(ir)
    

    return f"{int(p)} $"



def main():
    st.title("Uy narxlarini aniqlash")
    rooms = st.text_input("Xonalar soni")
    size = st.text_input("O'lchami kv(m)")
    level = st.text_input("Qavati")
    max_level = st.text_input("Umumiy qavat")
    

    pred = ''

    if st.button("Price"):
        r = int(rooms)
        s = int(size)
        l = int(level)
        m = int(max_level)
        pred = pre([r,s,l,m])
        

        st.success(pred)

if __name__ == '__main__':
    main()
