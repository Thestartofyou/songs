import mido
from mido import MidiFile, MidiTrack, Message
import time

# Define the MIDI port
output_port = mido.open_output()

# Define the notes and their corresponding MIDI values (adjust as needed)
notes = {'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69, 'B': 71}

def play_note(note, duration):
    # Send a note-on message
    output_port.send(Message('note_on', note=notes[note], velocity=64))

    # Wait for the specified duration
    time.sleep(duration)

    # Send a note-off message
    output_port.send(Message('note_off', note=notes[note], velocity=64))

# Example: "Twinkle, Twinkle, Little Star"
song_notes = ['C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C']

# Play each note with a duration of 0.5 seconds
for note in song_notes:
    play_note(note, 0.5)

# Close the MIDI port
output_port.close()

