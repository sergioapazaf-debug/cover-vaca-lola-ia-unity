# ============================================================
# EJECUCIÓN EN GOOGLE COLAB
# ============================================================
# Este script está pensado para copiarse en una notebook
# de Google Colab con GPU habilitada.
#
# Requisitos:
# - Cuenta de Hugging Face
# - Token de acceso de Hugging Face
# - GPU T4 o superior (recomendado)
# ============================================================

# ============================================================
# 1. AUTENTICACIÓN EN HUGGING FACE
# ============================================================
# Reemplazar por un token personal de Hugging Face.
# https://huggingface.co/settings/tokens

from huggingface_hub import login

login("YOUR_HUGGINGFACE_TOKEN")


# ============================================================
# 2. INSTALACIÓN DE DEPENDENCIAS
# ============================================================

!pip install omnivoice
!pip install soundfile


# ============================================================
# 3. CARGA DEL MODELO
# ============================================================

from omnivoice.models.omnivoice import OmniVoice

model = OmniVoice.from_pretrained(
    "ModelsLab/omnivoice-singing"
).to("cuda").eval()


# ============================================================
# 4. VERIFICAR DISPONIBILIDAD DE GPU
# ============================================================

import torch

print("GPU disponible:", torch.cuda.is_available())


# ============================================================
# 5. CARGAR AUDIO DE REFERENCIA
# ============================================================
# Subir un archivo de audio que servirá como referencia
# para la voz que se desea imitar.

from google.colab import files

uploaded = files.upload()

ref_audio_path = list(uploaded.keys())[0]


# ============================================================
# 6. LETRA DE LA CANCIÓN
# ============================================================
# Reemplazar el contenido según la canción deseada.

texto = """
La vacaa Lola,
Tienee cabezaa y tieene cola,
La vaca Lola,
Tienee cabezaa y tieene cola,
La vaca Lola,
La vaca Lola,
Tiene cabeza y tiene cola,
y hace mu
"""


# ============================================================
# 7. GENERACIÓN DEL AUDIO
# ============================================================

audios = model.generate(
    text=f"[singing]\n{texto}",
    language="Spanish",
    ref_audio=ref_audio_path,
    guidance_scale=0.5,
    duration=50
)


# ============================================================
# 8. GUARDAR RESULTADO EN WAV
# ============================================================

import soundfile as sf

sf.write(
    "out.wav",
    audios[0],
    model.sampling_rate
)


# ============================================================
# 9. DESCARGAR RESULTADO
# ============================================================

files.download("out.wav")