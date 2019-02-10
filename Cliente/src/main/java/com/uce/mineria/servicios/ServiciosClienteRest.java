package com.uce.mineria.servicios;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.List;

/*
 *Creado por: Bryan Saltos
 *    El: 23 - ene - 2019
 */
@Service
public class ServiciosClienteRest {

    RestTemplate template = new RestTemplate();
    List<String> lista = new ArrayList();

    public String prueba (String variables){
        String a = template.getForObject("http://localhost:1234/prediccion/<"+variables+">", String.class);
        System.out.println(a);
        a = a.replaceAll("\\D+","");
        System.out.println(a);
        return a;
    }




    public String clasificacionArbol (String variables){
        String b = template.getForObject("http://localhost:1234/clasificacionArbol/<"+variables+">", String.class);
        System.out.println(b);
        b=b.replaceAll("[^A-Za-z]", "");
        System.out.println(b);
        return b;
    }


    public String clasificacionMaquinaSoporteVectorial (String variables){
        String c = template.getForObject("http://localhost:1234/clasificacionMaquinaSoporteVectorial/<"+variables+">", String.class);
        System.out.println(c);
        c = c.replaceAll("[^A-Za-z]", "");
        System.out.println(c);
        return c;
    }


    public String clasificacionRegresionLogistica (String variables){
        String d = template.getForObject("http://localhost:1234/clasificacionRegresionLogistica/<"+variables+">", String.class);
        System.out.println(d);
        d = d.replaceAll("[^A-Za-z]", "");
        System.out.println(d);
        return d;
    }


    public String clasificacionVecinosCercanos (String variables){
        String e = template.getForObject("http://localhost:1234/clasificacionVecinosCercanos/<"+variables+">", String.class);
        System.out.println(e);
        e = e.replaceAll("[^A-Za-z]", "");
        System.out.println(e);
        return e;
    }


}
