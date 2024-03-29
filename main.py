from pytube import YouTube
from pathlib import Path
import os

print("#######################################################")
print("#################  YOUTUBE DOWNLOADER  ################")
print("#######       Criado por Matheus Tiburcio       #######")
print("#######################################################")
print('')

def fazerDownload(url, type):
    path = str(Path.home() / "Downloads")

    if(type == 'audio'):
      yt = YouTube(url)
      ys = yt.streams.filter(only_audio=True).first()
      print('Baixando...')
      out_file = ys.download(path)

      # Converter MP4 em MP3
      base, ext = os.path.splitext(out_file)
      new_file = base + '.mp3'
      os.rename(out_file, new_file)
      
      # Aviso
      print('A música foi baixada com sucesso, acesse a pasta de downloads!')
      print('\n===============================================================================')
      print('')

      menu()

    elif(type == 'video'):
      yt = YouTube(url)
      ys = yt.streams.filter(res="720p").first()
      print('Baixando...')
      ys.download(path)
      

      # Aviso 
      print('O vídeo foi baixado com sucesso, acesse a pasta de downloads!')
      print('\n===============================================================================')
      print('')
      menu()


def menu():
    
    print('Escolha uma opção abaixo')
    print('[1] Baixar música (MP3)')
    print('[2] Baixar vídeo (720P)')
    print('[3] Sair')
    print('')
    opcao = int(input('Digite a opção desejada: '))

    if(opcao == 1):
        url = input('Digite a URL da música: ')
        fazerDownload(url, 'audio')
    elif(opcao == 2):
        url = input('Digite a URL do vídeo: ')
        fazerDownload(url, 'video')
    elif(opcao == 3):
        exit()

menu()












		
