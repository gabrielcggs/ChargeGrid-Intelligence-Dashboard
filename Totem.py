import customtkinter as ctk
from tkinter import messagebox
from firestore_service import salvar_sessao_recarga



#======================================
#              Funções
#======================================


# PEGA OS DADOS DO FORMULÁRIO, SALVA NO FIRESTORE, E ABRE O PAINEL DE INFO
def salvar_tudo():
    modelo = entrada_modelo.get()
    porcentagem = entrada_porcentagem.get()
    kwh = entrada_kwh.get()

    if not modelo or not porcentagem or not kwh:
        messagebox.showwarning("Campos incompletos", "Preencha modelo, porcentagem e kWh antes de continuar.")
        return

    try:
        salvar_dados(modelo, porcentagem, kwh)
    except Exception as e:
        messagebox.showerror(
            "Erro ao salvar no Firebase",
            f"Não foi possível salvar a sessão de recarga.\n\nDetalhes: {e}",
        )
        return

    abrir_painel_informacoes()

# SALVA A SESSÃO DE RECARGA NO FIRESTORE (substitui o antigo JSON local)
def salvar_dados(modelo, porcentagem, kwh):
    salvar_sessao_recarga(modelo=modelo, porcentagem=porcentagem, kwh=kwh)


# ABRE O PAINEL DE INFORMAÇÕES DO CARRO
def abrir_painel_informacoes():
    from calculos_totem import ener_consumida,tempo_h,tempo_m,valor_total


    frame = ctk.CTkFrame(
        totem,
        width=1000,
        height=800
    )
    frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    frame.pack_propagate(False)


    titulo_info = ctk.CTkLabel(
        frame,
        text="Informações da Recarga",
        font=("Arial", 50)
    )
    titulo_info.pack(pady=(20,0))

    info_consumida = ctk.CTkLabel(
        frame,
        text=f"A energia que será consumida pelo carro é: {ener_consumida} kwh",
        font=("Arial", 30)
    )
    info_consumida.pack(pady=(40,0))

    info_tempo = ctk.CTkLabel(
        frame,
        text=f"O tempo total de recarga do carro é: {tempo_h}:{tempo_m:.2f}",
        font=("Arial", 30)
    )
    info_tempo.pack(pady=(40, 0))

    info_custo = ctk.CTkLabel(
        frame,
        text=f"O custo total da recarga é: R${valor_total:.2f} ",
        font=("Arial", 30)
    )
    info_custo.pack(pady=(40, 0))


#======================================
#     Configurações da janela
#======================================
ctk.set_appearance_mode("light")
totem = ctk.CTk()
totem.title("Totem - ChargeGrid Intelligence")
totem.attributes("-fullscreen", True)


titulo = ctk.CTkLabel(
    totem,
    text="GoodWe",
    font=("Arial", 100)
)
titulo.pack(pady=(20, 0))



#======================================
#      Modelo do Carro
#======================================
titulo_modelo = ctk.CTkLabel(
    totem,
    text="Informe o modelo do carro: ",
    font=("Arial", 40)
)
titulo_modelo.pack(pady=(100, 0))

entrada_modelo = ctk.CTkEntry(
    totem,
    width=1000,
    height=50,
    placeholder_text="Modelo"
)
entrada_modelo.pack(pady=(30, 0))




#======================================
#      Porcentagem do Carro
#======================================
titulo_porcentagem = ctk.CTkLabel(
    totem,
    text="Informe quantos porcento de bateria tem no carro: ",
    font=("Arial", 40)
)
titulo_porcentagem.pack(pady=(50, 0))

entrada_porcentagem = ctk.CTkEntry(
    totem,
    width=1000,
    height=50,
    placeholder_text="Porcentagem"
)
entrada_porcentagem.pack(pady=(30, 0))




#======================================
#      kWh do Carro
#======================================
titulo_kwh = ctk.CTkLabel(
    totem,
    text="Insira quantos quilo-watts(kWh) cabem no carro: ",
    font=("Arial", 40)
)
titulo_kwh.pack(pady=(50, 0))

entrada_kwh = ctk.CTkEntry(
    totem,
    width=1000,
    height=50,
    placeholder_text="kWh"
)
entrada_kwh.pack(pady=(30, 0))




#======================================
#            Botão
#======================================
botao_proximo = ctk.CTkButton(
    totem,
    text="Concluir",
    command=salvar_tudo,
    fg_color="red",
    hover_color="darkred",
    width=200,
    height=50,
)
botao_proximo.pack(pady=(100, 0))



totem.mainloop()