import streamlit as st
import pandas as pd
import sqlite3
import hashlib

conn = sqlite3.connect('database.db')
c = conn.cursor()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def main():
    # タイトル
    st.title('inspection ログイン機能')

    menu = ["HOME","LOGIN","SIGNUP"]
    choice = st.sidebar.selectbox("メニュー",menu)

    if choice == "HOME":
        st.subheader("home")

    elif choice == "LOGIN":
        st.subheader("LOGIN")

        username = st.sidebar.text_input("ユーザー名を入力")
        password = st.sidebar.text_input("パスワードを入力")
        if st.sidebar.button("LOGIN"):
            create_user()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:

                st.success("{}さんでログインしました".format(username))

            else:

                st.warning("ユーザー名かパスワードが間違っています")
        
    elif choice == "SIGNUP":
        st.subheader("新規作成")
        new_user = st.text_input("ユーザー名を入力")
        new_password = st.text_input("パスワードを入力", type='password')


        if st.button("SIGNUP"):
            create_user()
            add_user(new_user,make_hashes(new_password))
            st.success("アカウントを作成しました")
            st.info("ログイン画面からログインしてください")




if __name__ == '__main__':
    main()