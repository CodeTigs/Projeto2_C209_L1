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
