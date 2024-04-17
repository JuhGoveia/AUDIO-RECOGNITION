"""
**Link do vídeo: https://youtu.be/TeCPw4tFO04 **
"""
#pip install pyaudio
#pip install pyttsx3 pyglet
#pip install SpeechRecognition
#pip install playsound
#pip install gtts

from gtts import gTTS
import os
import time
import speech_recognition as sr

def text_to_speech(text, file_name, wait_time=2):
    tts = gTTS(text=text, lang='pt')
    tts.save(file_name)
    os.system(f'start {file_name}')
    
    # Adiciona uma pausa de 'wait_time' segundos após a reprodução do áudio
    time.sleep(wait_time)

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)  # Tempo de espera reduzido para 5 segundos

    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        return text.lower()

    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
        text_to_speech("Não foi possível entender a fala.", 'nao_entende_fala.mp3', wait_time=3)  # 3 segundos de espera 
        return None

def apresentar_opcoes(opcoes):
    print("Opções disponíveis:")
    
    for opcao, descricao in opcoes.items():
        print(f"Opção {opcao}: {descricao}")
        text_to_speech(f"Opção {opcao}: {descricao}", f'opcao_{opcao}.mp3', wait_time=6)  # 6 segundos de espera

def main():
    opcoes = {
        '1': 'Consulta ao saldo da conta',
        '2': 'Simulação de compra internacional',
        '3': 'Falar com um atendente',
        '4': 'Sair do atendimento'
    }

    saudacao = "Bem-vindo à QuantumFinance. Como posso ajudar você hoje?"
    text_to_speech(saudacao, 'saudacao.mp3', wait_time=5)  # 5 segundos de espera

    while True:
        apresentar_opcoes(opcoes)

        # Capturar e identificar a opção selecionada
        resposta = speech_to_text()

        if resposta:
            print(f"Você disse: '{resposta}'.")
            resposta_numerica = None

            # Verificar se a resposta contém um número correspondente a uma opção
            for opcao, descricao in opcoes.items():
                if opcao in resposta:
                    resposta_numerica = opcao
                    break

            # Opção "Sair do atendimento" selecionada, encerra o loop
            if resposta_numerica == '4':
                agradecimento = "Obrigado por utilizar os serviços da QuantumFinance."
                text_to_speech(agradecimento, 'agradecimento.mp3')
                break



            if resposta_numerica:
                # Adiciona a frase de resposta correspondente
                resposta_confirmacao = f"Você escolheu '{opcoes[resposta_numerica]}', correto?"
                text_to_speech(resposta_confirmacao, 'resposta_confirmacao.mp3', wait_time=4)  # 2 segundos de espera                
                resposta_confirmacao = speech_to_text()

                if resposta_confirmacao:
                    resposta_confirmacao = resposta_confirmacao.lower()
                    if resposta_confirmacao == "sim":
                        print("Ok.")
                        text_to_speech("OK.", 'ok.mp3', wait_time=2)  # 2 segundos de espera
                        break

                    elif resposta_confirmacao == "não":
                        print("Voltando ao menu...")
                        text_to_speech("Voltando ao menu", 'volta_menu.mp3', wait_time=2)  # 2 segundos de espera                        

                    else:
                        print("Desculpe, não entendi.")
                        text_to_speech("Desculpe, não entendi.", 'nao_entendi.mp3', wait_time=2)  # 2 segundos de espera

            else:
                print("Opção inválida. Tente novamente.")
                text_to_speech("Opção inválida. Tente novamente.", 'opcao_invalida.mp3', wait_time=2)  # 2 segundos de espera

if __name__ == "__main__":
    main()
