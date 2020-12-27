import winsound


freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"


def first_solution():
    split_notes = notes.split('-')
    for note in split_notes:
        freq = note.split(',')[0]
        duration = int(note.split(',')[1])
        winsound.Beep(freqs[freq], duration)


def second_solution():
    split_notes = notes.split('-')
    iter_notes = iter(split_notes)
    while True:
        try:
            note = next(iter_notes)
            freq = note.split(',')[0]
            duration = int(note.split(',')[1])
            winsound.Beep(freqs[freq], duration)
        except StopIteration as err:
            print(err)
            break


def main():
    first_solution()
    second_solution()


if __name__ == "__main__":
    main()
