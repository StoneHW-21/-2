# Voice Assistant Camera Wearable

Improved my previous [ESP32-CAM Semantic Search Wearable](https://github.com/xanderchinxyz/ESP32-CAM-Semantic-Search) by improving the physical design and adding a voice assistant powered by a [local multimodal large language model](https://www.ollama.com/library/moondream), [Groq](https://groq.com/) with Retrieval Augmented Generation (RAG), and the [VOSK speech recognition model](https://alphacephei.com/vosk/).

## Demo

## Setup and Installation:
### Hardware and Components
- 1 XIAO ESP32 S3 Sense board
- 1 [220 mAh LiPo battery](https://www.amazon.ca/dp/B0CKRBTW8Z?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- 1 3 way switch
- 1 [3D Printed Case + Lid](https://github.com/xanderchinxyz/Voice-Assistant-Camera-Wearable/tree/main/STL-Files)
- 2 Wires

Solder components like so:

## How It Works:
When the wearable is switched on and the user is connected to the software, the wearable will start taking pictures every 5 seconds which will be sent over via Bluetooth Low Energy (BLE). Once the picture is received it is sent to a multimodal local language model running on Ollama where it generates a description of the image. The image is saved and the file name and description are added to a vector database and data frame containing past image files and descriptions. If the user presses the wire to ask the wearable a question, the wearable will turn off the camera and start recording audio packets. These audio packets are sent via BLE and processed by VOSK to generate the user transcription query. This transcription query is vectorized to obtain relevant context from the vector database and the question and context are sent to Groq for a super-fast response with an appropriate answer. Once the response is received, a Text-To-Speech model reads out the response. The user can then ask follow up questions or press the wire to resume capturing images.

## Acknowledgements
Thank you to [OpenGlass](https://github.com/BasedHardware/OpenGlass) for open-sourcing their code which helped me in creating the embedded software for the XIAO ESP32 S3.
