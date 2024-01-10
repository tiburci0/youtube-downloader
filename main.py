from pytube import YouTube
from pathlib import Path

print("#############################################################")
print("########## BAIXE MÚSICAS DO YOUTUBE FÁCIL e RÁPIDO ##########")
print("################ Criado por Matheus Tiburcio ################")
print("#############################################################")
print('')

def baixarMusica():
    link = input('Digite a URL da música: ')
    path = str(Path.home() / "Downloads")
	
    yt = YouTube(link)

    ys = yt.streams.filter(only_audio=True).first()

    ys.download(path)
    
    print('O arquivo foi baixado e salvo na pasta de Downloads!')
    baixarMusica()

baixarMusica()










		
