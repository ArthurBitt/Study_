package MyStreaming.Calculos;

import MyStreaming.Modulos.TituloSuperClass;

public class CalculadoraDeTempo {
    private int tempoTotal;

    public int getTempoTotal() {
        return tempoTotal;
    }

    public void inclui(TituloSuperClass titulo){
     this.tempoTotal += titulo.getDuracaoEmMinutos();
    }
}
