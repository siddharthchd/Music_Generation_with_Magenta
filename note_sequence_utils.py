import os
import time
import magenta.music as mm
from magenta.music.protobuf.music_pb2 import NoteSequence
from visual_midi import Plotter
from typing import Union, List, Optional

# Write sequences as MIDI files to the output directory
def save_midi(sequences: Union[NoteSequence, List[NoteSequence]], output_dir: Optional[str] = None, prefix : str = "sequence"):

    output_dir = os.path.join("output", output_dir) if output_dir else "output"
    os.makedirs(output_dir, exist_ok=True)

    if not isinstance(sequences, list):
        sequences = [sequences]

    for (index, sequence) in enumerate(sequences):

        date_time = time.strftime("%Y-%m-%d_%H%M%S")
        filename = f"{prefix}_{index:02}_{date_time}.mid"

        path = os.path.join(output_dir, filename)
        mm.midi_io.note_sequence_to_midi_file(sequence, path)
        print("Generated midi : {}".format(os.path.abspath(path)))

# Write sequences as HTML plot files to the output directory

def save_plot(sequences: Union[NoteSequence, List[NoteSequence]], output_dir: Optional[str] = None, prefix: str = "sequence", **kwargs):

    output_dir = os.path.join("output", output_dir) if output_dir else "output"
    os.makedirs(output_dir, exist_ok=True)

    if not isinstance(sequences, list):
        sequences = [sequences]

    for (index, sequence) in enumerate(sequences):

        date_time = time.strftime("%Y-%m-%d_%H%M%S")
        filename = f"{prefix}_{index:02}_{date_time}.html"

        path = os.path.join(output_dir, filename)
        midi = mm.midi_io.note_sequence_to_pretty_midi(sequence)

        plotter = Plotter(**kwargs)
        plotter.save(midi, path)
        print("Generated plot : {}".format(os.path.abspath(path)))
