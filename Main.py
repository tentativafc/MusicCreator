__author__ = '56789'
import copy
import random

from music21 import chord as chor_mus21
from music21 import stream
from music21 import note as note_mus21
from music21 import midi

notes_scale = ["C", "D", "E", "F", "G", "A", "B"]
chords = []
sc = stream.Score()
p1 = stream.Part()
p1.id = 'part1'

p2 = stream.Part()
p2.id = 'part2'

cadencias = [[1, 3, 0], [1, 0, 3]]
len_cadencias = len(cadencias)
quarter_lengths = [.5, .25]
total = 16

if __name__ == '__main__':

    for i in range(0, len(notes_scale)):
        note = notes_scale[i] + str(4)
        notes = [note]
        idx_next_note = (i + 2) % 7
        note = notes_scale[idx_next_note] + str(5) if idx_next_note < i else notes_scale[idx_next_note] + str(4)
        notes.append(note)
        idx_next_note = (i + 4) % 7
        note = notes_scale[idx_next_note] + str(5) if idx_next_note < i else notes_scale[idx_next_note] + str(4)
        notes.append(note)
        chor = chor_mus21.Chord(notes)
        chords.append(chor)

    num_sequencias = 8

    for i in range(0, num_sequencias):
        cadencia = cadencias[random.randint(0, len_cadencias - 1)]

        num_times = [8, 3, 5]

        for i in range(0, len(cadencia)):
            chor = copy.deepcopy(chords[cadencia[i]])
            num_notas = num_times[i]

            pitches = chor.pitches

            for i in range(0, len(pitches)):
                idx_pitch = random.randint(0, len(pitches) - 1)
                note = note_mus21.Note(pitches[idx_pitch])
                note.quarterLength = .25
                p1.append(note)

            #root_note = note_mus21.Note(chor.root())
            #root_note.quarterLength = .25
            #p1.repeatAppend(root_note, num_notas)

            chor.quarterLength = num_notas * .5
            p2.append(chor)

    sc.insert(0, p1)
    sc.insert(0, p2)
    sc.show()

    mf = midi.translate.streamToMidiFile(sc)
    mf.open("music.midi", "wb")
    mf.write()
    mf.close
