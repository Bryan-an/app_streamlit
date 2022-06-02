# Importar la librería streamlit y darle un alias (st)
import streamlit as st

# Título
st.title("Aplicación para análisis de datos")

# Título de la barra lateral derecha (la flechita)
st.sidebar.title("Ingreso de parámetros")

# Widgets
numero1 = st.slider("Seleccione primer valor",
                    min_value=0, max_value=10, value=3)

# Hay que especificar el nombre de los argumentos
numero2 = st.slider("Seleccione segundo valor",
                    min_value=0, max_value=10, value=3, step=2)

# Suma de los valores de los widgets
resultado = numero1 + numero2

# Imprimir el resultado
st.write("El resultado de la suma es: ", resultado)

# Metrics
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
