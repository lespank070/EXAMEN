# kontakt_skjema.py - Enkel validering av kontaktskjema
# Laget for Aurora IT

# Funksjon som sjekker om e-posten er gyldig
def sjekk_epost(epost):
    if "@" in epost and "." in epost:
        return True
    else:
        return False

# Funksjon som sjekker at alle felt er fylt ut
def sjekk_skjema(navn, epost, melding):
    if navn == "":
        print("Feil: Du maa skrive inn et navn.")
        return False

    if sjekk_epost(epost) == False:
        print("Feil: Ugyldig e-postadresse.")
        return False

    if melding == "":
        print("Feil: Du maa skrive en melding.")
        return False

    # Alt er ok
    return True

# Funksjon som lagrer meldingen til en tekstfil
def lagre_melding(navn, epost, melding):
    fil = open("meldinger.txt", "a", encoding="utf-8")
    fil.write("Navn: " + navn + "\n")
    fil.write("E-post: " + epost + "\n")
    fil.write("Melding: " + melding + "\n")
    fil.write("---\n")
    fil.close()
    print("Meldingen er lagret!")

# ---- Hovedprogram ----
print("=== Aurora IT - Kontaktskjema ===")
print()

# Henter input fra brukeren
navn = input("Skriv inn navnet ditt: ")
epost = input("Skriv inn e-posten din: ")
melding = input("Skriv meldingen din: ")

# Sjekker og lagrer
if sjekk_skjema(navn, epost, melding):
    lagre_melding(navn, epost, melding)
    print("Takk, " + navn + "! Vi tar kontakt snart.")
else:
    print("Skjemaet ble ikke sendt. Prov igjen.")