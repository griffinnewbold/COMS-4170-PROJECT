from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs
import os 
from dotenv import load_dotenv 

load_dotenv('.env')

client = ElevenLabs(
  api_key = os.getenv('API_KEY')
)

audio = client.generate(
  text = "Hello Michael, this is Lydia telling you that you have been promoted!",
  voice = Voice(
    voice_id= 'ssZyXpffWtwv2555GuIR',
    settings=VoiceSettings(stability=0.5, similarity_boost=0.75, style=0.0, use_speaker_boost=True)
  )
)

play(audio)