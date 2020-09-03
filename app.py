import streamlit as st 
import pandas as pd
import joblib

model = open("RandomForestStress.pkl", "rb")
rf=joblib.load(model)

st.title("Propensão Aplicações em Períodos de Stress")
 
segmento_list=['Private','Alta Renda','Varejo']
suitability_list=['Conservador','Moderado','Arrojado']
geracao_list=['Veterano','Baby Boomer','Geração X','Geração Y','Geração Z']
sexo_list=['Masculino','Feminino']
est_civil_list=['Solteiro','Casado','Divorciado','Viuvo']
nacionalidade_list=['Brasileiro','Estrangeiro']
escolaridade_list=['Ensino Fundamental','Ensino Medio','Superior Completo','Pós Graduação']

columns_list=['saldo_inicio_periodo_stress',
'tipo_cliente_ALTA_RENDA', 
'tipo_cliente_PRIVATE',
'tipo_cliente_VAREJO', 
'suitability_Arrojado',
'suitability_Conservador', 
'suitability_Moderado', 
'geracao_ALPHA',
'geracao_BABY_BOOMERS', 
'geracao_GERACAO_X', 
'geracao_GERACAO_Y',
'geracao_GERACAO_Z', 
'geracao_VETERANO', 
'sexo_FEMININO',
'sexo_MASCULINO', 
'est_civil_CASADO', 
'est_civil_DIVORCIADO',
'est_civil_SOLTEIRO', 
'est_civil_VIUVO', 
'nacionalidade_BRASILEIRO',
'nacionalidade_ESTRANGEIRO', 
'escolaridade_ANALFABETO',
'escolaridade_DOUTORADO', 
'escolaridade_ENSINO_FUNDAMENTAL',
'escolaridade_ENSINO_MEDIO', 
'escolaridade_MESTRADO',
'escolaridade_POS_GRADUADO', 
'escolaridade_SUPERIOR_COMPLETO',
'escolaridade_SUPERIOR_EM_ANDAMENTO']

input_variables = pd.DataFrame([[0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], columns=columns_list)

segmento = st.selectbox('Segmento:', segmento_list)
suitability = st.selectbox('Perfil Suitability:', suitability_list)
geracao = st.selectbox('Geração:', geracao_list)
sexo = st.selectbox('Sexo:', sexo_list)
est_civil = st.selectbox('Estado Civil:', est_civil_list)
nacionalidade = st.selectbox('Nacionalidade:', nacionalidade_list)
escolaridade = st.selectbox('Escolaridade:', escolaridade_list)
investimentos = st.slider(label='Saldo em Aplicações', key='Saldo em Aplicações',value=10.0, min_value=0.0, max_value=1000.0, step=5.0, format="%.1f mil")  * 1000


st.write("Volume Total Investimentos do Cliente: ", '{:,.0f}'.format(investimentos))

input_variables.saldo_inicio_periodo_stress[0] = investimentos

if segmento == 'Private':
	input_variables.tipo_cliente_PRIVATE[0] = 1
elif segmento == 'Alta Renda':
	input_variables.tipo_cliente_ALTA_RENDA[0] = 1
elif segmento == 'Varejo':
	input_variables.tipo_cliente_VAREJO[0] = 1	

if suitability == 'Arrojado':
	input_variables.suitability_Arrojado[0] = 1
elif suitability == 'Conservador':
	input_variables.suitability_Conservador[0] = 1
elif suitability == 'Moderado':
	input_variables.suitability_Moderado[0] = 1

if geracao == 'Veterano':
	input_variables.geracao_VETERANO[0] = 1
elif geracao == 'Baby Boomer':
	input_variables.geracao_BABY_BOOMERS[0] = 1
elif geracao == 'Geração X':
	input_variables.geracao_GERACAO_X[0] = 1
elif geracao == 'Geração Y':
	input_variables.geracao_GERACAO_Y[0] = 1
elif geracao == 'Geração Z':
	input_variables.geracao_GERACAO_Z[0] = 1

if sexo == 'Masculino':
	input_variables.sexo_MASCULINO[0] = 1
elif sexo == 'Feminino':
	input_variables.sexo_FEMININO[0] = 1

if est_civil == 'Solteiro':
	input_variables.est_civil_SOLTEIRO[0] = 1
elif est_civil == 'Casado':
	input_variables.est_civil_CASADO[0] = 1
elif est_civil == 'Divorciado':
	input_variables.est_civil_DIVORCIADO[0] = 1
elif est_civil == 'Viuvo':
	input_variables.est_civil_VIUVO[0] = 1

if nacionalidade == 'Brasileiro':
	input_variables.nacionalidade_BRASILEIRO[0] = 1
elif nacionalidade == 'Estrangeiro':
	input_variables.nacionalidade_ESTRANGEIRO[0] = 1

if escolaridade == 'Ensino Fundamental':
	input_variables.escolaridade_ENSINO_FUNDAMENTAL[0] = 1
elif escolaridade == 'Ensino Medio':
	input_variables.escolaridade_ENSINO_MEDIO[0] = 1
elif escolaridade == 'Superior Completo':
	input_variables.escolaridade_SUPERIOR_COMPLETO[0] = 1
elif escolaridade == 'Pós Graduação':
	input_variables.escolaridade_POS_GRADUADO[0] = 1


prob = [row[1] for row in rf.predict_proba(input_variables)]

st.write("Probalidade do cliente aplicar em períodos de Stress é: ", '{:,.1f}'.format(prob[0] * 100) , "%")
