# import codon
from flask import Flask,request,render_template
import os

# # Trecho do codigo abaixo usa o codon para processamento paralelo
# @codon.jit
# def function_codon():
#     import openmp as omp

#     @omp.master   
#     def only_run_by_master_thread(): #Controla a thred principal
#         print('Master')

#     @omp.single
#     def only_run_by_single_thread(): #Controla a thred secundaria
#         print('Single Thred')

#     print('Python')


#     _@par(ordered=True)
#     for i in range(2): # Usa o multiparalelismo para executar as funções
#         only_run_by_master_thread()
#         only_run_by_single_thread()
# function_codon()

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def main():
    '''
        Função destinada a rendenrizar em forma de lista o parametro passado
    '''
    if request.method == 'POST':
        return os.listdir(f'{request.headers.get("dir")}')
         
    else:
        return render_template('index.html')     
