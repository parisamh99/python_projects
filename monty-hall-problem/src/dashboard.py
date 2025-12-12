import streamlit as st
from solution.monty_hall_solution import simulate_game

st.title(":zap: Monty hall simulation")

num_of_game=st.number_input("enter the number of game to simulate",
                min_value=1,max_value=100000,value=100)

col1,col2 = st.columns(2)
col1.subheader("win percentage without swtich")
col2.subheader("win percentage with swtich")


chart1 = col1.line_chart(x=None,y=None,height=400)
chart2 = col2.line_chart(x=None,y=None,height=400)

win_no_swtich = 0
win_with_swtich = 0

for i in range(num_of_game):
    num_of_win_without_switch,num_of_win_with_switch = simulate_game(1)
    win_no_swtich += num_of_win_without_switch
    win_with_swtich += num_of_win_with_switch
    
    chart1.add_rows([win_no_swtich/(i+1)])
    chart2.add_rows([win_with_swtich/(i+1)])

