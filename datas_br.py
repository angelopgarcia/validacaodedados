from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
         tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
         return tempo_cadastro