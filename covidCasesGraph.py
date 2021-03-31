import pandas as pd
import plotly_express as px

a=pd.read_csv("Copy+of+data+-+data.csv")
graph=px.scatter(a,x="date",y="cases",color="country",title="Covid cases in different Countries")
graph.show()
