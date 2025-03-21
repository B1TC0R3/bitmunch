# BitMunch

```
usage: python ./main.py [-h] -i INPUT [-p PADDING] [-e]
options:
  -h, --help            show this help message and exit
  -i, --input INPUT     The raw payload. Read from STDIN.
  -p, --padding PADDING
                        Execute mode only. Addes padding*2 to padding*10 encoded characters (randomized) to the front and back of the payload.
  -e, --exec            Make the payload self-execute when pasted into a browser terminal. No extra eval() required.
```
