package MyStreaming.Modulos;

public class TituloSuperClass {

    //Atributos privados
    private String nome;
    private int anoLancamento;
    private boolean incluidNoPlano;
    private static double somaAvaliacoes;
    private static int totalDeAvaliacoes;
    private int duracaoEmMinutos;
    private static int quantTitulosAssistidos; // uso do static

    public TituloSuperClass(String nome, int ano, int duracao, double nota){ //utilização de um construtor
        this.nome = nome;
        this.anoLancamento = ano;
        this.duracaoEmMinutos = duracao;
        TituloSuperClass.somaAvaliacoes += nota;
        TituloSuperClass.quantTitulosAssistidos += 1;
        TituloSuperClass.totalDeAvaliacoes ++;
    }

    //getters e setters
    public String getNome() {

        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getAnoLancamento() {
        return anoLancamento;
    }

    public boolean isIncluidNoPlano() {
        return incluidNoPlano;
    }

    public double getSomaAvaliacoes() {
        return somaAvaliacoes;
    }

    public int getTotalDeAvaliacoes() {
        return totalDeAvaliacoes;
    }

    public int getDuracaoEmMinutos() {
        return duracaoEmMinutos;
    }

    //static method para contador
    public static int getQuantFilmesAssistidos(){
        return TituloSuperClass.quantTitulosAssistidos;
    }

    //métodos
    public void exibeFichaTecnica(){
        System.out.println("Nome: "+ this.nome);
        System.out.println("Ano: "+this.anoLancamento);
        System.out.println("Duração: "+ this.anoLancamento + "min");
        System.out.println(somaAvaliacoes);
        System.out.println("Nota: "+ this.mediaAvaliacoes());
    }



    public double mediaAvaliacoes(){
        double media = somaAvaliacoes/totalDeAvaliacoes;
        return media;
    }
}
