package MyStreaming.Modulos;

public class SeriesPraticandoHerança extends TituloSuperClass{
    private int temporadas;
    private int espisodiosTemporada;
    private boolean Ativa;
    private int minEpisodio;


    @Override
    public void exibeFichaTecnica() {
            System.out.println("Nome: "+ this.getNome());
            System.out.println("Ano: "+ this.getAnoLancamento());
            System.out.println("Temporadas: "+ this.getTemporadas());
            System.out.println("Avalição: "+ getSomaAvaliacoes()/getTotalDeAvaliacoes());
            System.out.println("Nota: "+ this.mediaAvaliacoes());

    }

    public SeriesPraticandoHerança(String nome, int ano, int Temporadas, double nota) {
        super(nome, ano, Temporadas, nota);
        this.temporadas = Temporadas;
    }

    public int getTemporadas() {
        return temporadas;
    }

    public void setTemporadas(int temporadas) {
        this.temporadas = temporadas;
    }

    public boolean isAtiva() {
        return Ativa;
    }

    public void setAtiva(boolean ativa) {
        Ativa = ativa;
    }

    public int getMinEpisodio() {
        return minEpisodio;
    }

    public void setMinEpisodio(int minEpisodio) {
        this.minEpisodio = minEpisodio;
    }

    public int getEspisodiosTemporada() {
        return espisodiosTemporada;
    }

    public void setEspisodiosTemporada(int espisodiosTemporada) {
        this.espisodiosTemporada = espisodiosTemporada;
    }
}
