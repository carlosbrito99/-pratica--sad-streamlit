# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonte de Dados
# https://www.kaggle.com/datasets/whenamancodes/student-performance

# Especificando o título da página e o ícone
st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")

# sidebar
st.sidebar.title("Configurações de Exibição")

gsheets_show_id = st.sidebar.radio("Selecione o Dataset", ("Matemática", "Português"))

# Carregando o dataset
gsheets_math_id = "1392993996"
gsheets_portuguese_id = "0"

show_id = gsheets_math_id if gsheets_show_id == "Matemática" else gsheets_portuguese_id

gsheets_url = 'https://docs.google.com/spreadsheets/d/1pfqNNPJrB1QFcqUm5evvDeijycnuPFDztInZvl3nOyU/edit#gid=' + show_id
@st.cache_data(ttl=120)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(gsheets_url)

# 1
st.subheader("Qual é a média de idade dos alunos na escola GP?")
school_mean_age = data[data.school == 'GP']['age'].mean()
st.write(school_mean_age)

# 2
st.subheader("Qual é a moda do endereço dos alunos na escola MS?")
school_moda_address = data[data.school == 'MS']['address'].mode()
school_count_address = data[data.school == 'MS']['address'].count()
school_count_address_U = data[(data.school == 'MS') & (data.address == 'U')]['address'].count()
school_count_address_R = data[(data.school == 'MS') & (data.address == 'R')]['address'].count()
match school_moda_address.values[0]:
    case 'U':
        st.write("Urbano")
    case 'R':
        st.write("Rural")
    case _:
        st.write("Não informado")


# 3
st.subheader("Qual é a médiana do tempo de viagem dos alunos que estudam na escola GP?")
school_median_traveltime = data[data.school == 'GP']['traveltime'].median()
school_count_travel_time_under_15 = data[(data.school == 'GP') & (data.traveltime == 1.0)]['traveltime'].count()
school_count_travel_time_15_30 = data[(data.school == 'GP') & (data.traveltime == 2.0)]['traveltime'].count()
school_count_travel_time_30_60 = data[(data.school == 'GP') & (data.traveltime == 3.0)]['traveltime'].count()
school_count_travel_time_over_60 = data[(data.school == 'GP') & (data.traveltime == 4.0)]['traveltime'].count()
match school_median_traveltime:
    case 1.0:
        st.write("Menos de 15 minutos")
    case 2.0:
        st.write("Entre 15 e 30 minutos")
    case 3.0:
        st.write("Entre 30 minutos e 1 hora")
    case 4.0:
        st.write("Mais de 1 hora")
    case _:
        st.write("Não informado")




# 4
st.subheader("Qual é o desvio padrão da idade dos alunos que têm apoio educacional extra na escola MS?")
school_std_age = data[(data.school == 'MS') & (data.schoolsup == 'yes')]['age'].std()
if school_std_age == school_std_age:
    st.write(school_std_age)
else:
    st.write("Não informado")


# 5
st.subheader("Qual é a média do tempo semanal de estudo dos alunos cujos pais estão separados na escola GP?")
school_mean_studytime = data[(data.school == 'GP') & (data.Pstatus == 'A')]['studytime'].mean()
st.write(school_mean_studytime)
school_count_studytime_under_2 = data[(data.school == 'GP') & (data.studytime == 1.0) & (data.Pstatus == 'A')]['studytime'].count()
school_count_studytime_2_5 = data[(data.school == 'GP') & (data.studytime == 2.0) & (data.Pstatus == 'A')]['studytime'].count()
school_count_studytime_5_10 = data[(data.school == 'GP') & (data.studytime == 3.0) & (data.Pstatus == 'A')]['studytime'].count()
school_count_studytime_over_10 = data[(data.school == 'GP') & (data.studytime == 4.0) & (data.Pstatus == 'A')]['studytime'].count()


# 6
st.subheader("Qual é a moda do motivo pelo qual os alunos escolheram a escola MS?")
school_moda_reason = data[data.school == 'MS']['reason'].mode()
school_moda_reason_next_home = data[(data.school == 'MS') & (data.reason == 'home')]['reason'].count()
school_moda_reason_next_reputation = data[(data.school == 'MS') & (data.reason == 'reputation')]['reason'].count()
school_moda_reason_next_course = data[(data.school == 'MS') & (data.reason == 'course')]['reason'].count()
school_moda_reason_next_other = data[(data.school == 'MS') & (data.reason == 'other')]['reason'].count()
match school_moda_reason.values[0]:
    case 'home':
        st.write("Proximidade da casa")
    case 'reputation':
        st.write("Reputação da escola")
    case 'course':
        st.write("Preferência pelo curso")
    case 'other':
        st.write("Outros")
    case _:
        st.write("Não informado")

# 7
st.subheader("Qual é a mediana do número de faltas dos alunos que frequentam a escola GP?")
school_median_absences = data[data.school == 'GP']['absences'].median()
st.write(school_median_absences)


# 8
st.subheader("Qual é o desvio padrão do nível de saúde dos alunos que frequentam atividades extracurriculares na escola MS?")
school_std_health = data[(data.school == 'MS') & (data.activities == 'yes')]['health'].std()
st.write(school_std_health)
school_std_health_next_1 = data[(data.school == 'MS') & (data.health == 1.0) & (data.activities == 'yes')]['health'].count()
school_std_health_next_2 = data[(data.school == 'MS') & (data.health == 2.0) & (data.activities == 'yes')]['health'].count()
school_std_health_next_3 = data[(data.school == 'MS') & (data.health == 3.0) & (data.activities == 'yes')]['health'].count()
school_std_health_next_4 = data[(data.school == 'MS') & (data.health == 4.0) & (data.activities == 'yes')]['health'].count()
school_std_health_next_5 = data[(data.school == 'MS') & (data.health == 5.0) & (data.activities == 'yes')]['health'].count()

# 9
st.subheader("Quantos alunos já cumpriram as horas extracurriculares?")
school_count_activities = data[data.activities == 'yes']['activities'].count()
st.write(school_count_activities)

# 10
st.subheader("Qual é a moda do consumo de álcool dos alunos da escola MS durante a semana de trabalho?")
school_moda_workday_alcohol = data[data.school == 'MS']['Dalc'].mode()
school_moda_workday_alcohol_next_1 = data[(data.school == 'MS') & (data.Dalc == 1.0)]['Dalc'].count()
school_moda_workday_alcohol_next_2 = data[(data.school == 'MS') & (data.Dalc == 2.0)]['Dalc'].count()
school_moda_workday_alcohol_next_3 = data[(data.school == 'MS') & (data.Dalc == 3.0)]['Dalc'].count()
school_moda_workday_alcohol_next_4 = data[(data.school == 'MS') & (data.Dalc == 4.0)]['Dalc'].count()
school_moda_workday_alcohol_next_5 = data[(data.school == 'MS') & (data.Dalc == 5.0)]['Dalc'].count()
match school_moda_workday_alcohol.values[0]:
    case 1.0:
        st.write("Muito baixo")
    case 2.0:
        st.write("Baixo")
    case 3.0:
        st.write("Regular")
    case 4.0:
        st.write("Alto")
    case 5.0:
        st.write("Muito alto")
    case _:
        st.write("Não informado")