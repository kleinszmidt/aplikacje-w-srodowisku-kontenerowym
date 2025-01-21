import sys

if len(sys.argv) > 1:
    print(f"Argumenty: {', '.join(sys.argv[1:])}")
else:
    print("Uruchomiono skrypt bez argumentów!")
