# Cover Multimedia de La Vaca Lola con IA y Unity

Producción multimedia de la canción infantil **La Vaca Lola** utilizando generación de voz mediante inteligencia artificial y animación 3D en Unity.

El proyecto combina síntesis de voz basada en una muestra vocal de referencia, animación obtenida desde Mixamo y exportación WebGL para su ejecución en navegador.

## Características

- Generación de voz cantada mediante IA.
- Uso de una muestra vocal de referencia.
- Animación 3D desarrollada en Unity 6.
- Personaje y animación obtenidos desde Mixamo.
- Exportación WebGL para navegador.
- Exportación de video mediante Unity Recorder.

## Tecnologías utilizadas

### Generación de audio

- Python
- Google Colab
- Hugging Face
- OmniVoice Singing
- SoundFile
- GPU NVIDIA T4

### Desarrollo multimedia

- Unity 6
- Mixamo
- Unity Recorder
- WebGL

## Estructura del repositorio

```text
audio/
colab/
Build/
TemplateData/
index.html
unity.rar
README.md
```

### audio/

Contiene los audios utilizados durante el proyecto:

- Muestra vocal de referencia.
- Audio generado mediante OmniVoice Singing.

### colab/

Contiene el script utilizado para generar el audio.

> **Importante:** El archivo `colab/colab.py` no está pensado para ejecutarse directamente como una aplicación local. Debe copiarse y pegarse dentro de una notebook de Google Colab.

### Build/, TemplateData/ e index.html

Archivos generados por Unity para la exportación WebGL.

### unity.rar

Proyecto completo de Unity utilizado para desarrollar la animación.

## Generación del audio

La voz fue generada utilizando el modelo OmniVoice Singing ejecutado en Google Colab.

Para reproducir el procedimiento:

1. Crear una notebook en Google Colab.
2. Activar una GPU.
3. Copiar el contenido de `colab/colab.py`.
4. Configurar un token personal de Hugging Face.
5. Cargar un audio de referencia.
6. Ejecutar el proceso de generación.

El resultado será un archivo WAV con la interpretación generada.

## Ejecución WebGL

La aplicación puede ejecutarse mediante la exportación WebGL incluida en el repositorio.

### GitHub Pages

Una vez publicado:

```text
https://sergioapazaf-debug.github.io/cover-vaca-lola-ia-unity/
```
## Controles

La aplicación permite interactuar con la cámara para observar al personaje desde diferentes ángulos.

| Tecla | Acción |
|---------|---------|
| Espacio | Iniciar o reproducir la animación y el audio |
| W o Flecha Arriba | Acercar la cámara |
| S o Flecha Abajo | Alejar la cámara |
| A o Flecha Izquierda | Girar la cámara alrededor del personaje hacia la izquierda |
| D o Flecha Derecha | Girar la cámara alrededor del personaje hacia la derecha |

## Objetivo de la interacción

Los controles permiten inspeccionar la animación desde diferentes perspectivas mientras se reproduce el cover generado mediante inteligencia artificial.

### Ejecución local

También es posible utilizar los archivos:

```text
Build/
TemplateData/
index.html
```

mediante un servidor web local.

## Autor

Sergio Apaza