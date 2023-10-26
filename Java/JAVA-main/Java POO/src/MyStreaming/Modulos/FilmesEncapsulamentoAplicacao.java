package MyStreaming.Modulos;

public class FilmesEncapsulamentoAplicacao extends TituloSuperClass{
private String diretor;
private int oscars;

    public FilmesEncapsulamentoAplicacao(String nome, int ano, int duracao, double nota) {
        super(nome, ano, duracao, nota);
    }

    public String getDiretor() {
        return diretor;
    }

    public void setDiretor(String diretor) {
        this.diretor = diretor;
    }

    public int getOscars() {
        return oscars;
    }

    public void setOscars(int oscars) {
        this.oscars = oscars;
    }
}
