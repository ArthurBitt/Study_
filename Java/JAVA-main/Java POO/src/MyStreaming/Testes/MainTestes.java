package MyStreaming.Testes;

import MyStreaming.Modulos.FilmesPOO;
import MyStreaming.Modulos.FilmesEncapsulamentoAplicacao;
import MyStreaming.Modulos.SeriesPraticandoHerança;
import MyStreaming.Modulos.TituloSuperClass;

public class MainTestes {
    public static void main(String[] args) {
        //Classe filme sem encapsulamento
        FilmesPOO f1 = new FilmesPOO();
        f1.nome = "Evil Dead";
        f1.anoLancamento = 2023;
        f1.duracaoEmMinutos = 120;
        f1.avalia(10);
        f1.avalia(10);
        f1.avalia(10);


        f1.exibeFichaTecnica();
        System.out.println(f1.mediaAvaliacoes());

        //classe filme com encapsulamento
        FilmesEncapsulamentoAplicacao f2 = new FilmesEncapsulamentoAplicacao("The Grudge", 2001,115, 8);
        FilmesEncapsulamentoAplicacao f3 = new FilmesEncapsulamentoAplicacao("The Grudge", 2001,115, 8);
        FilmesEncapsulamentoAplicacao f4 = new FilmesEncapsulamentoAplicacao("The Grudge", 2001,115, 8);

        f2.setNome("Zumbiland");// usando set

        System.out.println(f2.getNome()); //printando um get

        int total = FilmesEncapsulamentoAplicacao.getQuantFilmesAssistidos();//definido a variavel para usar static
        System.out.println(f2.mediaAvaliacoes());

        //Class serie derivando de uma superclass Titulo
        SeriesPraticandoHerança Serie1 = new SeriesPraticandoHerança("The Walking Dead",2010,12,8.0);

        Serie1.exibeFichaTecnica();








        System.out.println(total);//printando um get

        
    }
}

