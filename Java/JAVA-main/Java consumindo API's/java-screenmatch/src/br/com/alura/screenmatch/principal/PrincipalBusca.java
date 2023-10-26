package br.com.alura.screenmatch.principal;

import br.com.alura.screenmatch.modelos.Titulo;
import com.google.gson.Gson;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class PrincipalBusca {
    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Busque um Titulo: ");
        var busca = sc.nextLine().replaceAll(" ", "+"); // formata padrão de busca
        String endereco = ("http://www.omdbapi.com/?t=" + busca + "&apikey=7a04b34b");// salva endereço com key
        HttpClient client = HttpClient.newHttpClient();// biblioteca client
        HttpRequest request = HttpRequest.newBuilder()//biblioteca request
                .uri(URI.create(endereco))// uri para busca do endereço da api web
                .build();//build

        HttpResponse<String> response = client //biblioteca response usando o client
                .send(request, HttpResponse.BodyHandlers.ofString());//traz o body das informações
        var json= response.body(); //json recebe body
        Gson gson = new Gson(); //intância repositório externo Gson para manipular arquivos json

        Titulo titleconvertfrom = gson.fromJson(json, Titulo.class); //método fromjson para conversão do body em
        // atributos da classe Titulo
        System.out.println(titleconvertfrom);



    }




}
