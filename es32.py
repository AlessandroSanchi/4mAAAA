class Utente:
    def __init__(self,nome,email,password,playlists,video,abbonamento) :
        self.nome = nome 
        self.email = email
        self.password = password
        self.playlists = []
        self.video = [] 
        self.abbonamento = abbonamento

    def CreaVideo(self,video):
        self.video.append(video) 
    def CreaPlaylist(self,Playlist):
        self.playlists.append(Playlist)
    def ScriviCommento(self, commento):
        if commento.video in self.video:
            commento.video.commenti.append(commento) 
    def CompraAbbonamento(self, abbonamento):
        self.abbonamento = abbonamento
    def InserisciVideoinPlaylist(self, video, playlist):
        if playlist in self.playlists:
            playlist.append(video)



class Abbonamento:
    def __init__(self,utente,tipo,prezzo,datainizio,datafine):
        self.utente = utente
        self.tipo = tipo
        self.prezzo = prezzo
        self.datainizio = datainizio
        self.datafine = datafine



class Playlist:
    def __init__(self,video,utente,nome):
        self.video = [video] 
        self.nome = nome 
        self.utente = utente

    def AggiungiVideo(self,video: "Video"):
        self.video.append(video)  
        print(f"Video '{video.titolo}' aggiunto alla playlist '{self.nome}'.")


class Video:
    def __init__(self,titolo,descrizione,url,durata,commenti,creatore):
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url 
        self.durata = durata
        self.commenti = commenti
        self.creatore = creatore

        




class Commento:
    def __init__(self,utente,testo,datadipubblicazione,video):
        self.utente = utente
        self.video = video 
        self.testo = testo
        self.datadipubblicazione = datadipubblicazione





if __name__ == "__main__":

    utente = Utente("Casaòs","weeeee@gmail.com","password",[Playlist],[Video],Abbonamento)
    video = Video("5 verifiche alla settimana, 0 cure al mese", "Quando Promos","httttttttpssnioiwbgeiugiweugheowwehowe",5.18,[],"Creatore")
    commento1 = Commento("Salame","Di pips out",12,video)
    commento2 = Commento("Rong","Di peruch out",12,video)
    playlist = Playlist(video,"0 errori", utente)
    abbonamento = Abbonamento("Casaòs","Premium",200,"2025-09-23","2026-09-23")
       
    utente.ScriviCommento(commento1)
    utente.ScriviCommento(commento2)

    utente.CreaVideo(video)
    utente.CreaPlaylist(playlist)