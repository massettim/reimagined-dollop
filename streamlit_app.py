import streamlit as st

st.write("""
# Welcome to Silverback Playground
Training indomitable beasts
""")

st.write("""
### DAY MEDIUM		

#### WARM UP
ROW: 3' TOTALI: 30'' SPRINT - 30'' EASY					
					
#### STRENGHT 

8 SET

BLOCK SNATCH UP THE KNEE + OH

2+1

START FROM 75%

REST 1'30" BETWEEN SET					
					
------          
         
PUSH PRESS

2 WAVE

5 @ 70%

3 @ 75%

1 @ 80% 


REST. 2' BETWEEN WAVE
""")
st.write("""
#### Calculate:
""")

weight = st.number_input('KG', min_value=0, value=100)
percentage = st.number_input('%', min_value=0.0, value=50.0)
st.text(weight * percentage/100)

st.write("""
#### GYM					
6 ROUND FOR TIME					
					
8 STRICT HSPU (OR 40% MAX REP UB)

10 OH SQUAT 60% 1 RM

SKI 200M

------          
REST 3' THEN 
------

10 ROUND

15 CAL ROW

5 RING M.U. 

------
THEN
------

FOR TIME
25+25 PISTOL SQUAT 

(25 SOLO DESTRA + 25 SOLO SINISTRA) 
					

#### AEROBIC CAPACITY	

800M RUN PACE 25 SEC: 100M 

REST 1'  E 30'' WALK

600M RUN PACE 25 SEC: 100M

REST.1' ( 30'' WALK)

RUN 400M PACE 20 SEC 100 M

REST.1'

RUN 800M PACE 25 SEC 100M

REST 2'

RUN  600M PACE 25 SEC 100M

REST 1'

RUN 400 M PACE 25 SEC 100M 

MEDIA PACE SCALATO 30-35 SEC

WOMAN 35-40 SEC 100
""")
			
st.write("""
## Finally...
""")		
if st.button('Push Here!',type="primary"):
	st.balloons()
	st.success("Fucking Amazing!", icon="🦍")

