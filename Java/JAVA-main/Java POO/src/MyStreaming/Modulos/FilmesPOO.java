package MyStreaming.Modulos;

public class FilmesPOO {
    public String nome;
    public int anoLancamento;
    boolean incluidNoPlano;
    double somaAvaliacoes;
    int totalDeAvaliacoes;
    public int duracaoEmMinutos;


    public void exibeFichaTecnica(){
        System.out.println("Nome: "+ this.nome);
        System.out.println("Ano: "+this.anoLancamento);
        System.out.println("Duração: "+ this.anoLancamento + "min");
    }

    public void avalia(double nota){
        this.somaAvaliacoes += nota; //será usado para média
        totalDeAvaliacoes++; // quant avaliaçõe - dividirá a soma
    }

   public double mediaAvaliacoes(){
        double media = somaAvaliacoes/totalDeAvaliacoes;
        return media;
    }

}
