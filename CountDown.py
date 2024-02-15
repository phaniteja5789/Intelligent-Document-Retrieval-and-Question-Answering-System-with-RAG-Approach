import streamlit as st
import time

def waitFor(N):
    ph = st.empty()
    for secs in range(N,0,-1):
        ss = secs%60
        ph.metric("Navigating to Next Page within", f"{ss:02d}")
        time.sleep(1)