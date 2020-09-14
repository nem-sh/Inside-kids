- TTS

  - 구글 클라우드 플랫폼에서 **Cloud Text to Speech API** 사용
  - 서비스 계정 등록
  - 키 발급(json 형식)
  - cloud sdk 설치 및 설정
    - https://cloud.google.com/sdk/docs/quickstarts
    - 마지막 체크박스 전체 선택(gcloud init 자동 실행)
  - 가상환경 만들기
  - `pip install --upgrade google-cloud-texttospeech`
  - 입력한 text가 오디오 파일로 저장

  ```python
  #!/usr/bin/env python
  
  # Copyright 2018 Google Inc. All Rights Reserved.
  #
  # Licensed under the Apache License, Version 2.0 (the "License");
  # you may not use this file except in compliance with the License.
  # You may obtain a copy of the License at
  #
  #      http://www.apache.org/licenses/LICENSE-2.0
  #
  # Unless required by applicable law or agreed to in writing, software
  # distributed under the License is distributed on an "AS IS" BASIS,
  # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  # See the License for the specific language governing permissions and
  # limitations under the License.
  
  """Google Cloud Text-To-Speech API sample application .
  
  Example usage:
      python quickstart.py
  """
  import io
  import os
  
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"구글 클라우드 플랫폼 키 json 파일 경로"
  
  def run_quickstart():
      # [START tts_quickstart]
      """Synthesizes speech from the input string of text or ssml.
  
      Note: ssml must be well-formed according to:
          https://www.w3.org/TR/speech-synthesis/
      """
      from google.cloud import texttospeech
  
      # Instantiates a client
      client = texttospeech.TextToSpeechClient()
  
      # Set the text input to be synthesized
      synthesis_input = texttospeech.SynthesisInput(text="안녕하세요 우리는 이모삼촌들입니다")
  
      # Build the voice request, select the language code ("en-US") and the ssml
      # voice gender ("neutral")
      voice = texttospeech.VoiceSelectionParams(
          language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
      )
  
      # Select the type of audio file you want returned
      audio_config = texttospeech.AudioConfig(
          audio_encoding=texttospeech.AudioEncoding.MP3
      )
  
      # Perform the text-to-speech request on the text input with the selected
      # voice parameters and audio file type
      response = client.synthesize_speech(
          input=synthesis_input, voice=voice, audio_config=audio_config
      )
  
      # The response's audio_content is binary.
      with open("output.mp3", "wb") as out:
          # Write the response to the output file.
          out.write(response.audio_content)
          print('Audio content written to file "output.mp3"')
      # [END tts_quickstart]
  
  
  if __name__ == "__main__":
      run_quickstart()
  
  ```

  - 참고 영상
    - https://www.youtube.com/watch?v=79_WXPWdaWE&ab_channel=%EB%A0%88%EC%9D%B4%EC%9B%90TVRaywonTV

- STT

  - 구글 클라우드 플랫폼에서 **Cloud Speech to Text API** 사용

  - 서비스 계정 등록

  - 키 발급(json 형식)

  - cloud sdk 설치 및 설정

    - https://cloud.google.com/sdk/docs/quickstarts
    - 마지막 체크박스 전체 선택

  - 가상환경 만들기

  - `pip install --upgrade google-cloud-speech`

  - `pip install pyaudio`

    - 에러 발생 시(윈도우 10에서 에러 발생 가능)
    - `pip install pipwin`
    - `pipwin install pyaudio` 

  - 말하면 command창에 text 출력

    ```python
    #!/usr/bin/env python
    
    # Copyright 2017 Google Inc. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Google Cloud Speech API sample application using the streaming API.
    NOTE: This module requires the additional dependency `pyaudio`. To install
    using pip:
        pip install pyaudio
    Example usage:
        python transcribe_streaming_mic.py
    """
    
    # [START speech_transcribe_streaming_mic]
    from __future__ import division
    
    import re
    import sys
    
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    import pyaudio
    from six.moves import queue
    
    import io
    import os
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"구글 클라우드 플랫폼 키 json 파일 경로"
    
    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms
    
    
    class MicrophoneStream(object):
        """Opens a recording stream as a generator yielding the audio chunks."""
        def __init__(self, rate, chunk):
            self._rate = rate
            self._chunk = chunk
    
            # Create a thread-safe buffer of audio data
            self._buff = queue.Queue()
            self.closed = True
    
        def __enter__(self):
            self._audio_interface = pyaudio.PyAudio()
            self._audio_stream = self._audio_interface.open(
                format=pyaudio.paInt16,
                # The API currently only supports 1-channel (mono) audio
                # https://goo.gl/z757pE
                channels=1, rate=self._rate,
                input=True, frames_per_buffer=self._chunk,
                # Run the audio stream asynchronously to fill the buffer object.
                # This is necessary so that the input device's buffer doesn't
                # overflow while the calling thread makes network requests, etc.
                stream_callback=self._fill_buffer,
            )
    
            self.closed = False
    
            return self
    
        def __exit__(self, type, value, traceback):
            self._audio_stream.stop_stream()
            self._audio_stream.close()
            self.closed = True
            # Signal the generator to terminate so that the client's
            # streaming_recognize method will not block the process termination.
            self._buff.put(None)
            self._audio_interface.terminate()
    
        def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
            """Continuously collect data from the audio stream, into the buffer."""
            self._buff.put(in_data)
            return None, pyaudio.paContinue
    
        def generator(self):
            while not self.closed:
                # Use a blocking get() to ensure there's at least one chunk of
                # data, and stop iteration if the chunk is None, indicating the
                # end of the audio stream.
                chunk = self._buff.get()
                if chunk is None:
                    return
                data = [chunk]
    
                # Now consume whatever other data's still buffered.
                while True:
                    try:
                        chunk = self._buff.get(block=False)
                        if chunk is None:
                            return
                        data.append(chunk)
                    except queue.Empty:
                        break
    
                yield b''.join(data)
    
    
    def listen_print_loop(responses):
        """Iterates through server responses and prints them.
        The responses passed is a generator that will block until a response
        is provided by the server.
        Each response may contain multiple results, and each result may contain
        multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
        print only the transcription for the top alternative of the top result.
        In this case, responses are provided for interim results as well. If the
        response is an interim one, print a line feed at the end of it, to allow
        the next result to overwrite it, until the response is a final one. For the
        final one, print a newline to preserve the finalized transcription.
        """
        num_chars_printed = 0
        for response in responses:
            if not response.results:
                continue
    
            # The `results` list is consecutive. For streaming, we only care about
            # the first result being considered, since once it's `is_final`, it
            # moves on to considering the next utterance.
            result = response.results[0]
            if not result.alternatives:
                continue
    
            # Display the transcription of the top alternative.
            transcript = result.alternatives[0].transcript
    
            # Display interim results, but with a carriage return at the end of the
            # line, so subsequent lines will overwrite them.
            #
            # If the previous result was longer than this one, we need to print
            # some extra spaces to overwrite the previous result
            overwrite_chars = ' ' * (num_chars_printed - len(transcript))
    
            if not result.is_final:
                sys.stdout.write(transcript + overwrite_chars + '\r')
                sys.stdout.flush()
    
                num_chars_printed = len(transcript)
    
            else:
                print(transcript + overwrite_chars)
    
                # Exit recognition if any of the transcribed phrases could be
                # one of our keywords.
                if re.search(r'\b(exit|quit)\b', transcript, re.I):
                    print('Exiting..')
                    break
    
                num_chars_printed = 0
    
    
    def main():
        # See http://g.co/cloud/speech/docs/languages
        # for a list of supported languages.
        language_code = 'ko-KR'  # a BCP-47 language tag
    
        client = speech.SpeechClient()
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code)
        streaming_config = types.StreamingRecognitionConfig(
            config=config,
            interim_results=True)
    
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (types.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)
    
            responses = client.streaming_recognize(streaming_config, requests)
    
            # Now, put the transcription responses to use.
            listen_print_loop(responses)
    
    
    if __name__ == '__main__':
        main()
    # [END speech_transcribe_streaming_mic]
    ```

  - wav 파일 내 음성이 command창에 text로 출력

    ```python
    #!/usr/bin/env python
    
    # Copyright 2016 Google Inc. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    
    def run_quickstart():
        # [START speech_quickstart]
        import io
        import os
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"구글 클라우드 플랫폼 키 json파일 경로"
    
        # Imports the Google Cloud client library
        # [START migration_import]
        from google.cloud import speech
        from google.cloud.speech import enums
        from google.cloud.speech import types
        # [END migration_import]
    
        # Instantiates a client
        # [START migration_client]
        client = speech.SpeechClient()
        # [END migration_client]
    
        # The name of the audio file to transcribe
        file_name = os.path.join(
            os.path.dirname(__file__),
            '.',
            'sample.wav')
    
        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
    
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='ko-KR',
            audio_channel_count=2)
    
        # Detects speech in the audio file
        response = client.recognize(config, audio)
    
        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript))
    
    
    if __name__ == '__main__':
        run_quickstart()
    ```

  - 참고 영상

    - https://www.youtube.com/watch?v=Ds-7D8d-FwA&ab_channel=%EB%A0%88%EC%9D%B4%EC%9B%90TVRaywonTV

  - 코드 실행 시 출력 값 아무것도 안나오는 오류

    - wav, mp3 등 오디오 파일 형식에 따라 config 설정이 다름(위의 코드는 wav에 맞춰서 설정 바꿔줌)

    - mp3의 경우 베타 버전에서만 지원(import, config 속성 바꿔야 함)

      ```py
      from google.cloud import speech_v1p1beta1 as speech
      client = speech.SpeechClient()
      ```