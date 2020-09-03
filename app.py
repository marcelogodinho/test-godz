import streamlit as st 
#import locale

#locale.setlocale(locale.LC_ALL, 'en_US')

#x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)

#st.sidebar.title("Features")
#parameter_list=['Sepal length (cm)','Sepal Width (cm)','Petal length (cm)','Petal Width (cm)']
#parameter_input_values=[] 
#parameter_default_values=['5.2','3.2','4.2','1.2']

#values=[]

#Display
#for parameter, parameter_df in zip(parameter_list, parameter_default_values):
# 
# values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
# parameter_input_values.append(values)

st.title("Variáveis:")
 
private_list=['Private','Alta Renda','Varejo']
suitability_list=['Conservador','Moderado','Arrojado']
geracao_list=['Veterano','Baby Boomer','Geração X','Geração Y','Geração Z']
sexo_list=['Masculino','Feminino']
est_civil_list=['Solteiro','Casado','Divorciado','Viuvo']
nacionalidade_list=['Brasileiro','Estrangeiro']
escolaridade_list=['Ensino Fundamental','Ensino Medio','Superior Completo','Pós Graduação']

st.selectbox('Segmento:', private_list)
st.selectbox('Perfil Suitability:', suitability_list)
st.selectbox('Geração:', geracao_list)
st.selectbox('Sexo:', sexo_list)
st.selectbox('Estado Civil:', est_civil_list)
st.selectbox('Nacionalidade:', nacionalidade_list)
st.selectbox('Escolaridade:', escolaridade_list)
valor = st.slider(label='Saldo em Aplicações', key='Saldo em Aplicações',value=10.0, min_value=0.0, max_value=100.0, step=0.5, format="%.1f mi")
#st.sidebar.selectbox('Selecione:', original_list)
#input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
#st.write('\n\n')

st.write("Valor Selecionado: ", '{:,.0f}'.format(valor*1000000))