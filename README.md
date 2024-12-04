# Projeto2_C209_L1
Tiago Rodrigues Plum Ferreira GEC 1996
# Video Manipulation Script

Este repositório contém um script em Python para manipulação de vídeos utilizando a biblioteca [MoviePy](https://zulko.github.io/moviepy/). O script aplica algumas edições a um vídeo de entrada, incluindo inversão de imagem, diminuição do som, cortes e reordenação de partes do vídeo.

## Funcionalidades

1. **Inversão Alternada de Imagem**: O vídeo é dividido em intervalos de 20 segundos. Em cada segundo intervalo (20-40s, 60-80s, etc.), a imagem é invertida horizontalmente.

2. **Diminuição Gradativa do Som**: O áudio é reduzido gradativamente ao longo do vídeo, criando um efeito de fade-out.

3. **Reordenação do Vídeo**: Após o primeiro minuto do vídeo, os 20 segundos seguintes são cortados e adicionados ao final do vídeo, criando uma nova sequência.

## Requisitos

- Python 3.x
- Bibliotecas necessárias: MoviePy e NumPy

Para instalar as dependências, execute:


pip install moviepy numpy


Como Usar
Coloque o vídeo que você deseja editar na mesma pasta do script e nomeie-o como Video_original.mp4.

Execute o script com Python:

pip install moviepy numpy

Como Usar


1 Coloque o vídeo que você deseja editar na mesma pasta do script e nomeie-o como Video_original.mp4.


2 Execute o script com Python:


python video_manipulation.py


3 O vídeo resultante será salvo com o nome Video_modificado.mp4 na mesma pasta.

Explicação do Código



Reordenação do Vídeo: Após o primeiro minuto do vídeo, os 20 segundos seguintes são cortados e adicionados ao final do vídeo, criando uma nova sequência.

Requisitos

Python 3.x

Bibliotecas necessárias: MoviePy e NumPy

Para instalar as dependências, execute:

pip install moviepy numpy

Como Usar

Coloque o vídeo que você deseja editar na mesma pasta do script e nomeie-o como Video_original.mp4.

Execute o script com Python:

python video_manipulation.py

O vídeo resultante será salvo com o nome Video_modificado.mp4 na mesma pasta.

Código

import moviepy.editor as mpe
import numpy as np

# Carregar o vídeo original
video = mpe.VideoFileClip("Video_original.mp4")

# Função para inverter a imagem no eixo horizontal
def flip_frame(frame):
    return np.fliplr(frame)

# Aplicar inversão de imagem de forma alternada a cada 20 segundos
flipped_clips = []
for t in range(0, int(video.duration), 20):
    start_time = t
    end_time = min(t + 20, video.duration)
    subclip = video.subclip(start_time, end_time)
    if (t // 20) % 2 == 1:
        subclip = subclip.fl_image(flip_frame)
    flipped_clips.append(subclip)

# Concatenar todos os clipes invertidos
video_inverted = mpe.concatenate_videoclips(flipped_clips)

# Diminuição do som de forma gradativa ao longo do vídeo
video_faded = video_inverted.audio_fadeout(video_inverted.duration)

# Fazer o corte após o primeiro minuto e inserir os 20 segundos cortados no final do vídeo
if video_faded.duration > 80:
    first_part = video_faded.subclip(0, 60)
    cut_part = video_faded.subclip(60, 80)
    remaining_part = video_faded.subclip(80, video_faded.duration)
    final_video = mpe.concatenate_videoclips([first_part, remaining_part, cut_part])
else:
    final_video = video_faded

# Salvar o vídeo final
final_video.write_videofile("Video_modificado.mp4", codec="libx264", audio_codec="aac")

Explicação do Código

1 Carregar o Vídeo Original: O script começa carregando o vídeo original chamado Video_original.mp4 usando a biblioteca MoviePy.

2 Função para Inverter a Imagem: Uma função flip_frame é definida para inverter a imagem no eixo horizontal, utilizando a função np.fliplr() da biblioteca NumPy.

3 Aplicar Inversão de Imagem Alternada: O vídeo é dividido em subclipes de 20 segundos cada. Cada segundo subclipe (ou seja, aqueles em posições ímpares) é processado para aplicar a inversão de imagem, criando um efeito alternado ao longo do vídeo.

4 Concatenar Todos os Clipes: Os subclipes (alguns invertidos e outros não) são concatenados para formar um único vídeo usando a função concatenate_videoclips do MoviePy.

5 Diminuição Gradativa do Som: Um efeito de fade-out é aplicado ao áudio do vídeo concatenado, de modo que o som diminui gradativamente até o final do vídeo.

6 Reordenação do Vídeo: Se a duração do vídeo for maior que 80 segundos, ele é dividido da seguinte forma:

 Os primeiros 60 segundos são mantidos.

 Os 20 segundos seguintes (entre 60 e 80) são cortados e movidos para o final do vídeo.

 A parte restante do vídeo (após os 80 segundos) é adicionada antes dos 20 segundos cortados.

7 Salvar o Vídeo Final: O vídeo final modificado é salvo com o nome Video_modificado.mp4, utilizando o codec libx264 e o codec de áudio aac para garantir qualidade e compatibilidade.
